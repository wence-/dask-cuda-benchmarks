# Per https://docs.nersc.gov/jobs/best-practices/#improve-efficiency-by-preparing-user-environment-before-running
# set up environment on login node

module load PrgEnv-nvidia
module load cudatoolkit
module load gcc

export PROTOCOL=ucx
export SCRATCH=/pscratch/sd/w/wence
export SCRATCHDIR=${SCRATCH}/dask-cuda-benchmark/scratch
export RUNDIR=/global/common/software/dasrepo/wence/src/dask-cuda-benchmarks/perlmutter-transpose/
mkdir -p ${SCRATCHDIR}

source /global/common/software/dasrepo/wence/mambaforge/etc/profile.d/conda.sh
source /global/common/software/dasrepo/wence/mambaforge/etc/profile.d/mamba.sh
mamba activate dask-cuda

echo "PATH=${PATH}"
echo "PROTOCOL=${PROTOCOL}"
echo "SCRATCHDIR=${SCRATCHDIR}"
export DASK_DISTRIBUTED__COMM__TIMEOUTS__CONNECT=3600s
export DASK_DISTRIBUTED__COMM__TIMEOUTS__TCP=3600s
export NUM_NODES=1
export DATA_SIZE=50000

# export NUM_NODES=2
# export DATA_SIZE=70000

# export NUM_NODES=4
# export DATA_SIZE=100000

# export NUM_NODES=8
# export DATA_SIZE=140000

# export NUM_NODES=16
# export DATA_SIZE=200000

# export NUM_NODES=32
# export DATA_SIZE=280000

# export NUM_NODES=64
# export DATA_SIZE=400000

export JOB_NAME=transpose
sbatch --job-name ${JOB_NAME} \
       --nodes ${NUM_NODES} \
       -e slurm-%x-%j.err \
       -o slurm-%x-%j.out \
       ./job.slurm
