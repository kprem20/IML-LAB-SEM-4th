import math

# Points
points = {
    'A': (2, 3),
    'B': (3, 4),
    'C': (6, 6),
    'D': (7, 7)
}

# Initial centroids
centroid1 = points['A']
centroid2 = points['C']

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Mean function
def mean(cluster):
    x = sum(p[0] for p in cluster) / len(cluster)
    y = sum(p[1] for p in cluster) / len(cluster)
    return (x, y)

# Iteration
while True:
    cluster1 = []
    cluster2 = []

    # Assign points to clusters
    for name, point in points.items():
        d1 = distance(point, centroid1)
        d2 = distance(point, centroid2)

        if d1 < d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # Compute new centroids
    new_centroid1 = mean(cluster1)
    new_centroid2 = mean(cluster2)

    print("Cluster 1:", cluster1)
    print("Cluster 2:", cluster2)
    print("Centroid 1:", new_centroid1)
    print("Centroid 2:", new_centroid2)
    print("------")

    # Stop condition
    if new_centroid1 == centroid1 and new_centroid2 == centroid2:
        break

    centroid1 = new_centroid1
    centroid2 = new_centroid2

# Final Output
print("\nFinal Clusters:")
print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Final Centroids:", centroid1, centroid2)