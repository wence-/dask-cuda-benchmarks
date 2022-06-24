#!/bin/bash
#SBATCH --qos=early_science
#SBATCH --account=dasrepo_g
#SBATCH --constraint=gpu
#SBATCH --gpus-per-node=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --time=00:15:00

module load PrgEnv-nvidia
module load cudatoolkit
module load gcc

export PROTOCOL=ucx

export SCRATCH=/pscratch/sd/w/wence
export OUTDIR=${SCRATCH}/dask-cuda-benchmark/output-${PROTOCOL}-${SLURM_JOB_NUM_NODES}
export SCRATCHDIR=${SCRATCH}/dask-cuda-benchmark/scratch
export RUNDIR=/global/common/software/dasrepo/wence/src/dask-cuda-benchmarks/perlmutter/


mkdir -p ${OUTDIR}
mkdir -p ${SCRATCHDIR}

srun job.sh
