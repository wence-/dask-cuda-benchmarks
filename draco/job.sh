#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh
source /opt/conda/etc/profile.d/mamba.sh
mamba activate ucx

SCHED_FILE=${SCRATCHDIR}/scheduler-${SLURM_JOBID}.json

NGPUS=$(nvidia-smi -L | wc -l)
export EXPECTED_NUM_WORKERS=$((SLURM_JOB_NUM_NODES * NGPUS))

# FIXME is the interface correct?
export COMMON_ARGS="--protocol ${PROTOCOL} \
       --interface ib0 \
       --scheduler-file ${SCRATCHDIR}/scheduler-${SLURM_JOBID}.json"
export PROTOCOL_ARGS=""
export WORKER_ARGS="--local-directory /tmp/dask-${SLURM_PROCID} \
       --multiprocessing-method forkserver"

export PTXCOMPILER_CHECK_NUMBA_CODEGEN_PATCH_NEEDED=0
export UCX_SOCKADDR_TLS_PRIORITY=rdmacm

# Submit with --gpus-per-node NGPU --ntasks-per-node 1 --cpus-per-task NGPU (or 2xNGPU)

# Idea: we allocate ntasks-per-node for workers, but those are started in the
# background by dask-cuda-worker.
# So we need to pick one process per node to run the worker commands.
# This assumes that the mapping from nodes to ranks is dense and contiguous. If
# there is rank-remapping then something more complicated would be needed.
if [[ $(((SLURM_PROCID / SLURM_NTASKS_PER_NODE) * SLURM_NTASKS_PER_NODE)) == ${SLURM_PROCID} ]]; then
    # rank zero starts scheduler and client as well
    if [[ $SLURM_NODEID == 0 ]]; then
        echo "${SLURM_PROCID} on node ${SLURM_NODEID} starting scheduler/client"
        python -m distributed.cli.dask_scheduler \
               --no-dashboard \
               ${COMMON_ARGS} &
        sleep 6
        python -m dask_cuda.cli.dask_cuda_worker \
               --no-dashboard \
               ${COMMON_ARGS} \
               ${PROTOCOL_ARGS} \
               ${WORKER_ARGS} &
        python ${RUNDIR}/local_cudf_merge.py \
               -c 40_000_000 \
               --frac-match 0.6 \
               --runs 10 \
               ${COMMON_ARGS} \
               ${PROTOCOL_ARGS} \
	       --backend dask \
               --shutdown-external-cluster-on-exit \
               --output-basename ${OUTDIR}/benchmark-data \
               --multiprocessing-method forkserver \
            || /bin/true        # always exit cleanly
    else
        echo "${SLURM_PROCID} on node ${SLURM_NODEID} starting worker"
        sleep 6
        python -m dask_cuda.cli.dask_cuda_worker \
               --no-dashboard \
               ${COMMON_ARGS} \
               ${PROTOCOL_ARGS} \
               ${WORKER_ARGS} \
            || /bin/true        # always exit cleanly
    fi
else
    echo "${SLURM_PROCID} on node ${SLURM_NODEID} sitting in background"
fi
