import numpy as np
from matplotlib import pyplot

osu_uni_bw_on_node = np.loadtxt("osu_uni_on_node.dat")

osu_bidi_bw_on_node = np.loadtxt("osu_bidi_on_node.dat")

osu_latency_on_node = np.loadtxt("osu_latency_on_node.dat")

osu_uni_bw_off_node = np.loadtxt("osu_uni_off_node.dat")

osu_bidi_bw_off_node = np.loadtxt("osu_bidi_off_node.dat")

osu_latency_off_node = np.loadtxt("osu_latency_off_node.dat")

ucx_uni_bw_on_node = np.loadtxt("ucx_uni_on_node.dat")

ucx_uni_bw_off_node = np.loadtxt("ucx_uni_off_node.dat")

ucx_latency_on_node = np.loadtxt("ucx_latency_on_node.dat")

ucx_latency_off_node = np.loadtxt("ucx_latency_off_node.dat")

ucxpy_core_bidi_bw_on_node = np.loadtxt("ucxpy_core_bidi_on_node.dat")

ucxpy_core_bidi_bw_off_node = np.loadtxt("ucxpy_core_bidi_off_node.dat")

ucxpy_bidi_bw_on_node = np.loadtxt("ucxpy_bidi_on_node.dat")

ucxpy_bidi_bw_off_node = np.loadtxt("ucxpy_bidi_off_node.dat")

ucxpy_core_latency_on_node = np.loadtxt("ucxpy_core_latency_on_node.dat")

ucxpy_latency_on_node = np.loadtxt("ucxpy_latency_on_node.dat")

ucxpy_core_latency_off_node = np.loadtxt("ucxpy_core_latency_off_node.dat")

ucxpy_latency_off_node = np.loadtxt("ucxpy_latency_off_node.dat")

fig, axes = pyplot.subplots(1)

axes.plot(
    osu_uni_bw_on_node[:, 0],
    osu_uni_bw_on_node[:, 1] / 1e6,
    linestyle="-",
    marker="o",
    label="osu_bw",
)
axes.plot(
    osu_bidi_bw_on_node[:, 0],
    osu_bidi_bw_on_node[:, 1] / 1e6,
    linestyle="-",
    marker="s",
    label="osu_bibw",
)

axes.plot(
    ucx_uni_bw_on_node[:, 0],
    ucx_uni_bw_on_node[:, 1] / 1e6,
    linestyle="-.",
    marker="v",
    label="ucx_perftest tag_bw"
)

axes.plot(
    ucxpy_core_bidi_bw_on_node[:, 0],
    ucxpy_core_bidi_bw_on_node[:, 1] / 1e6,
    linestyle="--",
    marker="^",
    label="UCXPy core bidi",
)

axes.plot(
    ucxpy_bidi_bw_on_node[:, 0],
    ucxpy_bidi_bw_on_node[:, 1] / 1e6,
    linestyle="--",
    marker="d",
    label="UCXPy bidi",
)

axes.set_xlabel("Message size [bytes]")
axes.set_ylabel("Bandwidth [MB/s]")

axes.set_xscale("log", base=2)
axes.set_yscale("log", base=10)

# 4 A100 GPUs, 4 NVLink connections between each device, each with
# 25GB/s unidirectional bandwidth, see
# https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/
#
#  0---1
#  |\ /|
#  | x |
#  |/ \|
#  2---3
axes.axhline(y=100e3, label="Uni BW hardware peak", linestyle="--")
axes.axhline(y=200e3, label="Bidi BW hardware peak", linestyle="-.")
axes.legend(loc="best")

axes.set_title("p2p on-node bandwidth (dev-0 to dev-1)")

fig.savefig("on-node-bandwidth.pdf")

fig, axes = pyplot.subplots(1)

axes.plot(
    osu_uni_bw_off_node[:, 0],
    osu_uni_bw_off_node[:, 1] / 1e6,
    linestyle="-",
    marker="o",
    label="osu_bw",
)
axes.plot(
    osu_bidi_bw_off_node[:, 0],
    osu_bidi_bw_off_node[:, 1] / 1e6,
    linestyle="-",
    marker="s",
    label="osu_bibw",
)

axes.plot(
    ucx_uni_bw_off_node[:, 0],
    ucx_uni_bw_off_node[:, 1] / 1e6,
    linestyle="-.",
    marker="v",
    label="ucx_perftest tag_bw"
)

axes.plot(
    ucxpy_core_bidi_bw_off_node[:, 0],
    ucxpy_core_bidi_bw_off_node[:, 1] / 1e6,
    linestyle="--",
    marker="^",
    label="UCXPy core bidi",
)

axes.plot(
    ucxpy_bidi_bw_off_node[:, 0],
    ucxpy_bidi_bw_off_node[:, 1] / 1e6,
    linestyle="--",
    marker="d",
    label="UCXPy bidi",
)

axes.set_xlabel("Message size [bytes]")
axes.set_ylabel("Bandwidth [MB/s]")

axes.set_xscale("log", base=2)
axes.set_yscale("log", base=10)

axes.legend(loc="best")

axes.set_title("p2p off-node bandwidth (dev-0 to dev-0)")

fig.savefig("off-node-bandwidth.pdf")

fig, axes = pyplot.subplots(1)

axes.plot(
    osu_latency_on_node[:, 0],
    osu_latency_on_node[:, 1],
    linestyle="-",
    marker="o",
    label="osu_latency (on node)",
)
axes.plot(
    osu_latency_off_node[:, 0],
    osu_latency_off_node[:, 1],
    linestyle="-",
    marker="s",
    label="osu_latency (off node)",
)
axes.plot(
    ucx_latency_on_node[:, 0],
    ucx_latency_on_node[:, 1],
    linestyle="-",
    marker="o",
    label="ucx_perftest tag_lat (on node)",
)
axes.plot(
    ucx_latency_off_node[:, 0],
    ucx_latency_off_node[:, 1],
    linestyle="-",
    marker="s",
    label="ucx_perftest tag_lat (off node)",
)

axes.plot(
    ucxpy_core_latency_on_node[:, 0],
    ucxpy_core_latency_on_node[:, 1],
    linestyle="--",
    marker="^",
    label="UCXPy core on node",
)

axes.plot(
    ucxpy_core_latency_off_node[:, 0],
    ucxpy_core_latency_off_node[:, 1],
    linestyle="--",
    marker="v",
    label="UCXPy core off node",
)

axes.plot(
    ucxpy_latency_on_node[:, 0],
    ucxpy_latency_on_node[:, 1],
    linestyle="--",
    marker="d",
    label="UCXPy on node",
)

axes.plot(
    ucxpy_latency_off_node[:, 0],
    ucxpy_latency_off_node[:, 1],
    linestyle="--",
    marker="x",
    label="UCXPy on node",
)

axes.set_xlabel("Message size [bytes]")
axes.set_ylabel("Message latency [μs]")

axes.set_xscale("log", base=2)
axes.set_yscale("log", base=10)

axes.legend(loc="best")

axes.set_title(
    "Point to point 1/2-ping-pong latency\n"
    "(dev-0 to dev-1 on node, dev-0 to dev-0 off node)"
)

fig.savefig("message-latency.pdf")
