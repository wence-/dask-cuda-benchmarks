import os
import sys
from pprint import pprint

import cupy as xp
from dask import array as da
from dask.distributed import Client, wait


def get_workers(dask_scheduler=None):
    return dask_scheduler.workers


def run():
    with Client(scheduler_file=os.path.abspath(sys.argv[1])) as client:
        while len(client.scheduler_info()["workers"]) < int(
            os.environ["EXPECTED_NUM_WORKERS"]
        ):
            print(
                "Waiting for workers to come up, "
                f"have {len(client.scheduler_info()['workers'])}, "
                f"want {os.environ['EXPECTED_NUM_WORKERS']}"
            )
        #     time.sleep(5)
        rs = da.random.RandomState(RandomState=xp.random.RandomState)
        x = rs.random((2500, 2500), chunks=1000).persist()
        wait(x)
        fn = lambda x: (x + x.T).sum()
        print("start")
        wait(client.persist(fn(x)))
        print("stop")
        workers = client.run_on_scheduler(get_workers)
        for worker in workers.values():
            pprint(worker)
            pprint(worker.name)
        print("Shutting down scheduler/workers")
        client.shutdown()
        client.close()


if __name__ == "__main__":
    run()
