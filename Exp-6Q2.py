import numpy as np

# Data
data = np.array([2, 4, 10, 12, 3, 20, 30, 11, 25])

# Initial centroids
C1, C2 = 2, 20

while True:
    
    # Assign points to clusters
    C1_points = [x for x in data if abs(x - C1) <= abs(x - C2)]
    C2_points = [x for x in data if abs(x - C1) > abs(x - C2)]

    # Compute new centroids
    new_C1 = np.mean(C1_points)
    new_C2 = np.mean(C2_points)

    print("Cluster 1:", C1_points, "Centroid:", new_C1)
    print("Cluster 2:", C2_points, "Centroid:", new_C2)
    print("------")

    # Stop condition
    if new_C1 == C1 and new_C2 == C2:
        break

    # Update centroids
    C1, C2 = new_C1, new_C2

# Final Output
print("\nFinal Result:")
print("Cluster 1:", C1_points, "Centroid:", C1)
print("Cluster 2:", C2_points, "Centroid:", C2)