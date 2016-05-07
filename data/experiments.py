import pandas as pd

import numpy as np
import matplotlib

def parse_time(timestring):
    return datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M:%S")

sift = {
    1: {"start": "2016-05-06T11:55:54", "end": "2016-05-06T12:17:13"},
    2: {"start": "2016-05-06T11:23:44", "end": "2016-05-06T11:44:29"},
    3: {"start": "2016-05-06T10:07:03", "end": "2016-05-06T10:26:10"},
    4: {"start": "2016-05-06T13:55:27", "end": "2016-05-06T14:08:47"},
}

def sift():
    sift_series = pd.Series({
        1: 1279,
        2: 1245,
        3: 1147,
        4: 800,
        })

    sift_plot = sift_series.plot(title="SIFT Running Time (Caltech-256)", colormap='jet', markersize=10, xticks=[1, 2, 3, 4], 
                                 style=["--bo"], yticks=[500, 700, 900, 1100, 1300])
    sift_plot.set_xlabel("Number of nodes")
    sift_plot.set_ylabel("Running time (Seconds)")

    matplotlib.pylab.show()

def sift10x():
    sift_10x_series = pd.Series({
    #    1: No Data,
        2: 6124,
        3: 4549,
        4: 3792,
        })

    sift_10x_plot = sift_10x_series.plot(title="SIFT Running Time (Caltech-256 x 10)", colormap='jet', markersize=10, xticks=[1, 2, 3, 4], 
                                     style=["--bo"], yticks=[3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500])
    sift_10x_plot.set_xlabel("Number of nodes")
    sift_10x_plot.set_ylabel("Running time (Seconds)")

    matplotlib.pylab.show()

def bow():
    sift_series = pd.Series({
        1: 1729,
        2: 991,
        3: 668,
        4: 477,
        })

    sift_plot = sift_series.plot(title="BoW Dictionary Learning (Caltech-256) K=2000", colormap='jet', markersize=10, xticks=[1, 2, 3, 4], 
                                 style=["--bo"], yticks=[400, 700, 1000, 1300, 1600, 1900])
    sift_plot.set_xlabel("Number of nodes")
    sift_plot.set_ylabel("Running time (Minutes)")

    matplotlib.pylab.show()

def alluxio():
    d = {"No Alluxio": [100, 100, 100, 100, 100],
         "Alluxio": [82.8, 101.5, 37.1, 95.4, 61.2]}
    df = pd.DataFrame(d, index=["SIFT", "BoW.L", "BoW.A", "Class.L", "Class.P"])

    ax = df.plot(kind="bar", title="Alluxio performance comparison", legend=True)
    ax.set_xlabel("CloudVision Application")
    ax.set_ylabel("Normalized running time")
    matplotlib.pyplot.tight_layout()


    matplotlib.pyplot.show()


