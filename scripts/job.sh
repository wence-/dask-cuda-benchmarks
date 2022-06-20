#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh
source /opt/conda/etc/profile.d/mamba.sh
mamba activate ucx

SCHED_FILE=${SCRATCHDIR}/scheduler-${SLURM_JOBID}.json

NGPUS=$(nvidia-smi -L | wc -l)
export EXPECTED_NUM_WORKERS=$((SLURM_JOB_NUM_NODES * NGPUS))

# Idea: we allocate ntasks-per-node for workers, but those are started in the
# background by dask-cuda-worker.
# So we need to pick one process per node to run the worker commands.
# This assumes that the mapping from nodes to ranks is dense and contiguous. If
# there is rank-remapping then something more complicated would be needed.
if [[ $(((SLURM_PROCID / SLURM_NTASKS_PER_NODE) * SLURM_PROCID)) == $SLURM_PROCID ]]; then
    # rank zero starts scheduler and client as well
    if [[ $SLURM_NODEID == 0 ]]; then
        echo "${SLURM_PROCID} on node ${SLURM_NODEID} starting scheduler/client"
        dask-scheduler --scheduler-file ${SCHED_FILE} &
        sleep 6
        dask-cuda-worker --scheduler-file ${SCHED_FILE} &
        python ${RUNDIR}/hello.py ${SCHED_FILE}
    else
        echo "${SLURM_PROCID} on node ${SLURM_NODEID} starting worker"
        sleep 6
        dask-cuda-worker --scheduler-file ${SCHED_FILE}
    fi
else
    echo "${SLURM_PROCID} on node ${SLURM_NODEID} sitting in background"
fi
