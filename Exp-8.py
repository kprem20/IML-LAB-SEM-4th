data = [2, 4, 5, 10, 12]
medoids = [2, 10]

def assign(data, medoids):
    clusters = {m: [] for m in medoids}
    for p in data:
        d = [abs(p - m) for m in medoids]
        clusters[medoids[d.index(min(d))]].append(p)
    return clusters

def update(clusters):
    new_medoids = []
    for cluster in clusters.values():
        costs = []
        for p in cluster:
            cost = sum(abs(p - x) for x in cluster)
            costs.append(cost)
        new_medoids.append(cluster[costs.index(min(costs))])
    return new_medoids


clusters = assign(data, medoids)
new_medoids = update(clusters)
clusters = assign(data, new_medoids)

print("Final Medoids:", new_medoids)
print("Clusters:", clusters)
