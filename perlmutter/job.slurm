#!/bin/bash
#SBATCH --qos=early_science
#SBATCH --account=dasrepo_g
#SBATCH --constraint=gpu
#SBATCH --gpus-per-node=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --time=00:15:00

export SCRATCH=/pscratch/sd/w/wence
export OUTDIR=${SCRATCH}/dask-cuda-benchmark/output
export SCRATCHDIR=${SCRATCH}/dask-cuda-benchmark/scratch
export RUNDIR=/global/common/software/dasrepo/wence/src/dask-cuda-benchmarks/perlmutter/


mkdir -p ${OUTDIR}
mkdir -p ${SCRATCHDIR}

srun job.sh
