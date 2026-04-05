import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

points = np.array([
    [1, 2],  
    [2, 1],  
    [4, 3],  
    [5, 4]   
])


Z = linkage(points, method='single', metric='euclidean')

dendrogram(Z, labels=['A', 'B', 'C', 'D'])

plt.title("Dendrogram (Agglomerative Clustering)")
plt.xlabel("Points")
plt.ylabel("Distance")
plt.show()
