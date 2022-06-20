#!/bin/bash
#SBATCH -p WHATEVER
#SBATCH -A sw_rapids_testing
#SBATCH --nv-meta=ml-model.rapids-debug
#SBATCH --gpus-per-node 8
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 16

RUNDIR_HOST=$(pwd)
OUTDIR_HOST=$(readlink `pwd`/../outputs)
SCRATCHDIR_HOST=$(readlink `pwd`/../scratch)
mkdir -p ${OUTDIR_HOST}
mkdir -p ${SCRATCHDIR_HOST}

export RUNDIR=/root/rundir
export OUTDIR=/root/outdir
export SCRATCHDIR=/root/scratchdir

JOB_SCRIPT=${RUNDIR_CONTAINER}/job.sh


srun --container-image=IMAGE.sqsh --no-container-mount-home \
     --container-mounts=${RUNDIR_HOST}:${RUNDIR}:ro,${OUTDIR_HOST}:${OUTDIR}:rw,${SCRATCHDIR_HOST}:${SCRATCHDIR}:rw \
     ${JOB_SCRIPT}
