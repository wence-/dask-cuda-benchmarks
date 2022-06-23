#!/bin/bash
#SBATCH -p batch_dgx1_m2
#SBATCH -A sw_rapids_testing
#SBATCH --nv-meta=ml-model.rapids-debug
#SBATCH --gpus-per-node 8
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 16

export RUNDIR_HOST=$(readlink -f `pwd`)
export OUTDIR_HOST=$(readlink -f `pwd`/outputs)
export SCRATCHDIR_HOST=$(readlink -f `pwd`/scratch)
mkdir -p ${OUTDIR_HOST}
mkdir -p ${SCRATCHDIR_HOST}

export RUNDIR=/root/rundir
export OUTDIR=/root/outdir
export SCRATCHDIR=/root/scratchdir

export JOB_SCRIPT=${RUNDIR}/job.sh

export CONTAINER=$(readlink -f ~/workdir/ucx-py-new.sqsh)

srun --container-image=${CONTAINER} --no-container-mount-home \
     --container-mounts=${RUNDIR_HOST}:${RUNDIR}:ro,${OUTDIR_HOST}:${OUTDIR}:rw,${SCRATCHDIR_HOST}:${SCRATCHDIR}:rw \
     ${JOB_SCRIPT}
