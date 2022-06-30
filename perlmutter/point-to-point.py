import numpy as np
from matplotlib import pyplot

osu_uni_bw_on_node = np.fromstring(
    """
1                       0.03e6
2                       0.06e6
4                       0.13e6
8                       0.26e6
16                      0.53e6
32                      1.06e6
64                      2.12e6
128                     4.19e6
256                     8.41e6
512                    16.91e6
1024                   40.97e6
2048                   81.73e6
4096                  162.32e6
8192                  322.77e6
16384                 643.77e6
32768                1272.71e6
65536                2488.46e6
131072               4814.73e6
262144               9145.92e6
524288              16540.49e6
1048576             28185.33e6
2097152             44078.42e6
4194304             59830.63e6
8388608             73082.26e6
16777216            81857.39e6
33554432            87577.29e6
67108864            90450.37e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

osu_bidi_bw_on_node = np.fromstring(
    """
1                       0.13e6
2                       0.27e6
4                       0.54e6
8                       1.08e6
16                      2.15e6
32                      4.27e6
64                      8.47e6
128                    16.85e6
256                    33.51e6
512                    67.09e6
1024                  312.66e6
2048                  623.28e6
4096                 1243.06e6
8192                 2465.91e6
16384                4921.15e6
32768                9770.16e6
65536               18432.64e6
131072              33509.94e6
262144              58175.06e6
524288              93885.56e6
1048576            129575.66e6
2097152            155414.99e6
4194304            165600.20e6
8388608            171833.95e6
16777216           174637.42e6
33554432           176084.09e6
67108864           176888.27e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

osu_latency_on_node = np.fromstring(
    """
1                      14.66
2                      14.58
4                      14.54
8                      14.59
16                     14.63
32                     14.65
64                     14.71
128                    14.74
256                    14.77
512                    14.83
1024                    9.68
2048                    9.68
4096                    9.79
8192                    9.89
16384                  10.07
32768                  10.11
65536                  10.68
131072                 11.65
262144                 13.15
524288                 15.73
1048576                21.29
2097152                32.28
4194304                54.71
8388608                99.02
16777216              187.59
33554432              366.31
67108864              723.12
""".strip(),
    sep=" ",
).reshape(-1, 2)

osu_uni_bw_off_node = np.fromstring(
    """
1                       0.03e6
2                       0.05e6
4                       0.11e6
8                       0.22e6
16                      0.43e6
32                      0.87e6
64                      1.74e6
128                     3.46e6
256                     6.84e6
512                    18.17e6
1024                   36.04e6
2048                   71.90e6
4096                  140.12e6
8192                  275.38e6
16384                 525.92e6
32768                 991.10e6
65536                1809.47e6
131072               3203.21e6
262144               4943.57e6
524288               7077.73e6
1048576              8794.38e6
2097152             10254.80e6
4194304             10959.21e6
8388608             11632.62e6
16777216            11593.00e6
33554432            11859.22e6
67108864            10009.68e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

osu_bidi_bw_off_node = np.fromstring(
    """
1                       0.11e6
2                       0.21e6
4                       0.42e6
8                       0.85e6
16                      1.65e6
32                      3.40e6
64                      6.80e6
128                    13.61e6
256                    26.13e6
512                   102.19e6
1024                  204.77e6
2048                  397.81e6
4096                  732.81e6
8192                 1394.89e6
16384                2572.04e6
32768                4271.94e6
65536                7518.33e6
131072              11155.59e6
262144              14053.89e6
524288              15886.83e6
1048576             15982.74e6
2097152             18299.32e6
4194304             18713.68e6
8388608             18576.39e6
16777216            18936.18e6
33554432            16499.92e6
67108864            16532.26e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

osu_latency_off_node = np.fromstring(
    """
1                      18.17
2                      18.10
4                      18.11
8                      18.13
16                     18.35
32                     18.35
64                     18.46
128                    18.61
256                    19.22
512                     9.68
1024                    9.79
2048                   10.09
4096                   10.77
8192                   11.42
16384                  12.54
32768                  14.55
65536                  17.29
131072                 22.75
262144                 34.12
524288                 56.39
1048576               100.70
2097152               188.20
4194304               363.00
8388608               714.83
16777216             1414.51
33554432             3357.35
67108864             6668.94
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_core_bidi_bw_on_node = np.fromstring(
    """
1                0.12e6
2                0.25e6
4                0.48e6
8                0.98e6
16               1.94e6
32               3.92e6
64               7.94e6
128             14.98e6
256             31.07e6
512             61.43e6
1024           119.67e6
2048           241.26e6
4096           429.31e6
8192           399.57e6
16384          792.46e6
32768         1578.40e6
65536         3124.59e6
131072        5884.11e6
262144       11231.34e6
524288       19628.00e6
1048576      33264.52e6
2097152      48543.87e6
4194304      64188.29e6
8388608      76514.84e6
16777216     84385.37e6
33554432     88669.60e6
67108864     91257.32e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_core_bidi_bw_off_node = np.fromstring(
    """
1                0.11e6
2                0.23e6
4                0.42e6
8                0.88e6
16               1.86e6
32               3.55e6
64               7.06e6
128             14.31e6
256             28.14e6
512             55.77e6
1024           104.77e6
2048           220.92e6
4096           398.94e6
8192           518.88e6
16384          960.20e6
32768         1750.20e6
65536         2866.89e6
131072        4928.47e6
262144        6914.90e6
524288        8847.63e6
1048576      10146.86e6
2097152      11156.18e6
4194304      11650.10e6
8388608      11800.42e6
16777216     12047.38e6
33554432     11370.93e6
67108864     10587.09e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_bidi_bw_on_node = np.fromstring(
    """
1                0.02e6
2                0.04e6
4                0.07e6
8                0.14e6
16               0.30e6
32               0.58e6
64               1.17e6
128              2.34e6
256              4.65e6
512              9.23e6
1024            19.00e6
2048            37.61e6
4096            74.94e6
8192           110.79e6
16384          221.75e6
32768          449.34e6
65536          885.97e6
131072        1803.89e6
262144        3543.35e6
524288        6796.79e6
1048576       9814.00e6
2097152      19477.68e6
4194304      24126.98e6
8388608      37430.64e6
16777216     53322.02e6
33554432     67914.17e6
67108864     77663.75e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_bidi_bw_off_node = np.fromstring(
    """
1                0.02e6
2                0.04e6
4                0.07e6
8                0.15e6
16               0.29e6
32               0.58e6
64               1.15e6
128              2.20e6
256              4.48e6
512              9.31e6
1024            18.29e6
2048            37.28e6
4096            73.11e6
8192           130.11e6
16384          245.27e6
32768          454.41e6
65536          878.42e6
131072        1471.03e6
262144        2652.14e6
524288        4348.65e6
1048576       6292.13e6
2097152       8235.60e6
4194304       9846.21e6
8388608      10855.53e6
16777216     11370.93e6
33554432     10909.22e6
67108864     10286.45e6
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_core_latency_on_node = np.fromstring(
    """
1                8.76
2                8.43
4                8.37
8                8.47
16               8.37
32               8.52
64               8.78
128              8.58
256              8.82
512              8.50
1024             8.82
2048             8.71
4096             9.36
8192            20.62
16384           20.26
32768           20.68
65536           21.26
131072          21.49
262144          22.97
524288          25.36
1048576         31.60
2097152         42.26
4194304         65.43
8388608        109.73
16777216       199.24
33554432       378.05
67108864       735.89
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_latency_on_node = np.fromstring(
    """
1               52.90
2               52.32
4               53.09
8               53.78
16              54.20
32              52.91
64              53.55
128             53.83
256             53.71
512             53.32
1024            53.56
2048            54.16
4096            53.72
8192            73.29
16384           72.74
32768           73.09
65536           74.18
131072          74.80
262144          90.94
524288          77.52
1048576         97.78
2097152        109.31
4194304        170.76
8388608        220.52
16777216       310.31
33554432       488.21
67108864       851.00
""".strip(),
    sep=" ",
).reshape(-1, 2)

ucxpy_core_latency_off_node = np.fromstring("""
1             9.12
2            10.43
4             8.61
8             8.61
16            9.32
32            8.82
64            9.27
128           9.15
256           9.03
512           9.24
1024          9.57
2048          9.78
4096          9.98
8192         15.74
16384        16.63
32768        18.70
65536        21.60
131072       28.30
262144       38.02
524288       60.05
1048576     102.89
2097152     188.16
4194304     359.79
8388608     703.70
16777216    1.39e3
33554432    2.94e3
67108864    6.30e3
""".strip(), sep=" ").reshape(-1, 2)

ucxpy_latency_off_node = np.fromstring("""
1             54.68
2             55.48
4             55.38
8             54.19
16            57.71
32            55.29
64            55.44
128           54.17
256           55.38
512           58.16
1024          59.88
2048          56.10
4096          57.35
8192          65.99
16384         69.87
32768         70.27
65536         73.89
131072        86.67
262144       100.30
524288       121.61
1048576      167.90
2097152      257.54
4194304      428.30
8388608      774.10
16777216     1.48e3
33554432     3.07e3
67108864     6.52e3
""".strip(), sep=" ").reshape(-1, 2)

fig, axes = pyplot.subplots(1)

axes.plot(
    osu_uni_bw_on_node[:, 0],
    osu_uni_bw_on_node[:, 1] / 1e6,
    linestyle="-",
    marker="o",
    label="OSU uni",
)
axes.plot(
    osu_bidi_bw_on_node[:, 0],
    osu_bidi_bw_on_node[:, 1] / 1e6,
    linestyle="-",
    marker="s",
    label="OSU bidi",
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

axes.legend(loc="best")

axes.set_title("p2p on-node bandwidth (dev-0 to dev-1)")

fig.savefig("on-node-bandwidth.pdf")

fig, axes = pyplot.subplots(1)

axes.plot(
    osu_uni_bw_off_node[:, 0],
    osu_uni_bw_off_node[:, 1] / 1e6,
    linestyle="-",
    marker="o",
    label="OSU uni",
)
axes.plot(
    osu_bidi_bw_off_node[:, 0],
    osu_bidi_bw_off_node[:, 1] / 1e6,
    linestyle="-",
    marker="s",
    label="OSU bidi",
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
    label="OSU on node",
)
axes.plot(
    osu_latency_off_node[:, 0],
    osu_latency_off_node[:, 1],
    linestyle="-",
    marker="s",
    label="OSU off node",
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
