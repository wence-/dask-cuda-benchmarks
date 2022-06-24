#!/bin/bash
#SBATCH --qos=early_science
#SBATCH --account=dasrepo_g
#SBATCH --constraint=gpu
#SBATCH --gpus-per-task=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --time=00:15:00

export OUTDIR=${SCRATCH}/dask-cuda-benchmark/output-${PROTOCOL}-${SLURM_JOB_NUM_NODES}-${SLURM_JOB_ID}

mkdir -p ${OUTDIR}

srun job.sh

rsync --delete -rupm ${SCRATCH}/dask-cuda-benchmark/ ${HOME}/benchmark-results/ --filter '- scratch/'
