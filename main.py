import plotly.plotly as py
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import numpy as np
from scipy.spatial.distance import pdist
import scipy.spatial.distance as H
from sklearn.cluster import KMeans
import pylab as P


def optics_alg(x, k, distMethod='euclidean'): #was euclidean
    if len(x.shape) > 1:
        m, n = x.shape
    else:
        m = x.shape[0]
        n == 1

    try:
        D = H.squareform(pdist(x, distMethod))
        distOK = True
    except:
        print("squareform or pdist error")
        distOK = False

    CD = np.zeros(m)
    RD = np.ones(m) * 1E10

    for i in range(m):
        tempInd = D[i].argsort()
        tempD = D[i][tempInd]
        CD[i] = tempD[k]

    order = []
    seeds = np.arange(m, dtype=np.int)

    ind = 0
    while len(seeds) != 1:
        ob = seeds[ind]
        seedInd = np.where(seeds != ob)
        seeds = seeds[seedInd]

        order.append(ob)
        tempX = np.ones(len(seeds)) * CD[ob]
        tempD = D[ob][seeds]  # [seeds]

        temp = np.column_stack((tempX, tempD))
        mm = np.max(temp, axis=1)
        ii = np.where(RD[seeds] > mm)[0]
        RD[seeds[ii]] = mm[ii]
        ind = np.argmin(RD[seeds])

    order.append(seeds[0])
    RD[0] = 0  # we set this point to 0 as it does not get overwritten
    return RD, CD, order
    
    
def plot_optics(ordered_reachabilities):

    trace = Bar(x=list(range(0, len(ordered_reachabilities))), y=ordered_reachabilities)
    data = [trace]
    layout = Layout(title='Optics algoritme')
    fig = Figure(data=data, layout=layout)
    iplot(fig)


RD, CD, order = optics_alg(data, 10)
ordered_reachabilities = RD[order]
plot_optics(ordered_reachabilities)    
