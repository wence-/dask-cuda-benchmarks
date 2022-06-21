import os
import sys
from pprint import pprint

import cupy as xp
import time
import sortedcontainers.sorteddict
from dask import array as da
from dask.distributed import Client, wait

def get_workers(dask_scheduler=None):
    return dask_scheduler.workers


def run():
    with Client(scheduler_file=os.path.abspath(sys.argv[1])) as client:
        while len(client.scheduler_info().get("workers", [])) < int(
            os.environ["EXPECTED_NUM_WORKERS"]
        ):
            print(
                "Waiting for workers to come up, "
                f"have {len(client.scheduler_info().get('workers', []))}, "
                f"want {os.environ['EXPECTED_NUM_WORKERS']}"
            )
            time.sleep(5)
        try:
            workers = client.run_on_scheduler(get_workers)
            for worker in workers.values():
                pprint(worker)
                pprint(worker.name)
        except Exception as e:
            print("run on scheduler failed, but meh.")
            print(e)
        print("Shutting down scheduler/workers")
        client.shutdown()
        client.close()


if __name__ == "__main__":
    run()
