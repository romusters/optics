# Ordering Points To Identify the Clustering Structure (OPTICS)

OPTICS is, like DBSCAN, a density based clustering method, but with one less parameter. In the original OPTICS paper, a reachability plot is created to aid the identification of clusters. 

# OPTICS vs Kmeans
Kmeans is often used on Real world data. Sometimes the data is not isotropically distributed, meaning the real-world clusters are not circular and uniformly distributed in all directions. Real-world data is often anisotropically distributed, meaning the real-world clusters are spherical and non-uniformly distributed. 

Kmeans uses a distance measure such as the Euclidean distance where density based clustering methods use the density.

# Reachability plot
The OPTICS algorithm starts with some point with a high density and searches for points which are reachable. The algorithm thus employs a bottom up strategy.

The peaks indicate cluster borders and the valleys between peaks indicate clusters.

The reachability plot gives insight into the structure of the clusters. Questions such as: Is there hierarchy? What is the variance? How many clusters are there? are easily answered.


# Source
Ankerst, M., Breunig, M. M., Kriegel, H. P., & Sander, J. (1999, June). OPTICS: ordering points to identify the clustering structure. In ACM Sigmod record (Vol. 28, No. 2, pp. 49-60). ACM.

# Credits
The python code is adapted from: http://chemometria.us.edu.pl/download/optics.py
Which I found in this repo: https://github.com/amyxzhang/OPTICS-Automatic-Clustering
