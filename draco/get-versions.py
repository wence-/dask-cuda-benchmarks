import json
import subprocess

import click


def get_versions():
    import cudf
    import cupy
    import dask
    import dask_cuda
    import distributed
    import numpy
    import rmm
    import ucp

    ucx_info, *_ = (
        subprocess.check_output(["ucx_info", "-v"]).decode().strip().split("\n")
    )
    *_, ucx_revision = ucx_info.split(" ")

    return {
        "numpy": numpy.__version__,
        "cupy": cupy.__version__,
        "rmm": rmm.__version__,
        "ucp": ucp.__version__,
        "ucx": ucx_revision,
        "dask": dask.__version__,
        "distributed": distributed.__version__,
        "dask_cuda": dask_cuda.__version,
        "cudf": cudf.__version__,
    }


@click.command()
@click.argument(
    "output_file", type=str, required=True, help="Output file name for version data"
)
def main(output_file):
    with open(output_file, "w") as f:
        json.dump(get_versions(), f)


if __name__ == "__main__":
    main()
