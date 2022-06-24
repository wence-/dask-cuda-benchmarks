# Per https://docs.nersc.gov/jobs/best-practices/#improve-efficiency-by-preparing-user-environment-before-running
# set up environment on login node

module load PrgEnv-nvidia
module load cudatoolkit
module load gcc

export PROTOCOL=ucx
export SCRATCH=/pscratch/sd/w/wence
export SCRATCHDIR=${SCRATCH}/dask-cuda-benchmark/scratch
export RUNDIR=/global/common/software/dasrepo/wence/src/dask-cuda-benchmarks/perlmutter/
mkdir -p ${SCRATCHDIR}

source /global/common/software/dasrepo/wence/mambaforge/etc/profile.d/conda.sh
source /global/common/software/dasrepo/wence/mambaforge/etc/profile.d/mamba.sh
mamba activate dask-cuda

sbatch --nodes 1 ./job.slurm
