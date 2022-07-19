import os
import glob
from itertools import chain
import pandas as pd
import click
import altair as alt

def remove_warmup(df):
    summary = df.groupby("num_workers")
    return df.loc[
        df.wallclock.values
        < (summary.wallclock.mean() + summary.wallclock.std() * 2)[
            df.num_workers
        ].values
    ]


def process_output(directories):
    all_merge_data = []
    all_transpose_data = []
    for d in directories:
        _, date, ucx_version = d.split("/")
        date = pd.to_datetime(date)
        dfs = []
        for f in chain(
            glob.glob(os.path.join(d, "nnodes*cudf-merge-dask.json")),
            glob.glob(os.path.join(d, "nnodes*cudf-merge-explicit-comms.json")),
        ):
            merge_df = pd.read_json(f)
            dfs.append(merge_df)
        merge_df = pd.concat(dfs, ignore_index=True)
        merge_df["date"] = date
        merge_df["ucx_version"] = ucx_version
        all_merge_data.append(merge_df)
        dfs = []
        for f in glob.glob(os.path.join(d, "nnodes*transpose-sum.json")):
            transpose_df = pd.read_json(f)
            dfs.append(transpose_df)
        transpose_df = pd.concat(dfs, ignore_index=True)
        transpose_df["date"] = date
        transpose_df["ucx_version"] = ucx_version
        all_transpose_data.append(transpose_df)

    merge_df = pd.concat(all_merge_data, ignore_index=True)
    transpose_df = pd.concat(all_transpose_data, ignore_index=True)
    return merge_df, transpose_df


def summarise_merge_data(df):
    dask = df.loc[lambda df: df.backend == "dask"]
    explicit = df.loc[lambda df: df.backend == "explicit-comms"]
    dask = remove_warmup(dask)
    explicit = remove_warmup(explicit)
    data = pd.concat([dask, explicit], ignore_index=True)
    data = data.groupby(["num_workers", "backend", "date"], as_index=False).mean()
    data["throughput"] = (data.data_processed / data.wallclock / data.num_workers) / 1e9
    tmp = data.loc[lambda df: df.backend == "dask"].copy()
    tmp["backend"] = "no-dask"
    # distributed-joins measurements
    for n, bw in zip(
        [8, 16, 32, 64, 128, 256],
        [5.4875, 4.325, 3.56875, 2.884375, 2.090625, 1.71835937],
    ):
        tmp.loc[lambda df: df.num_workers == n, "throughput"] = bw

    return pd.concat([data, tmp], ignore_index=True)


def summarise_transpose_data(df):
    df = remove_warmup(df)
    df = df.groupby(["num_workers", "date"], as_index=False).mean()
    df["throughput"] = (df.data_processed / df.wallclock / df.num_workers) / 1e9
    return df

def make_merge_chart(df):
    return (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(
            x=alt.X("date:T", title="Date"),
            y=alt.Y("throughput:Q", title="Throughput (GB/s/GPU)"),
            color="backend:N",
        )
        .facet(facet=alt.Text("num_workers:N", title="Number of GPUs"), columns=3)
    )


def make_transpose_chart(df):
    return (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(
            x=alt.X("date:T", title="Date"),
            y=alt.Y("throughput:Q", title="Throughput (GB/s/GPU)"),
        )
        .facet(facet=alt.Text("num_workers:N", title="Number of GPUs"), columns=3)
    )


@click.command()
@click.argument("merge_filename")
@click.argument("transpose_filename")
@click.option("--charts/--no-charts",
              type=bool,
              default=False,
              help="Make charts?")
def main(merge_filename, transpose_filename, charts):
    directories = glob.glob("outputs/*/ucx-1.12.1")
    merge, transpose = process_output(directories)
    merge = summarise_merge_data(merge)
    transpose = summarise_transpose_data(transpose)
    merge.to_json(merge_filename)
    transpose.to_json(transpose_filename)
    if charts:
        merge = make_merge_chart(merge)
        transpose = make_transpose_chart(transpose)
        merge.save(f"{os.path.basename(merge_filename)}.html")
        transpose.save(f"{os.path.basename(transpose_filename)}.html")

    
if __name__ == "__main__":
    main()
