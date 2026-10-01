# Credit to https://www.geeksforgeeks.org/dsa/bellman-ford-algorithm-simple-implementation/ for some inspiration.
# n(nodes) m(edges)
n, m = map(int, input().split())

graph = []
# Size n + 1 because points are 1-indexed. since a route can begin anywhere.
dist = [0] * (n + 1)

for _ in range(m):
    edge = tuple(map(int, input().split()))
    graph.append(edge)
    # Form (from, to, weight)

for _ in range(n - 1):
    for u, v, weight in graph:
        if dist[u]+weight > dist[v]:
            dist[v] = dist[u] + weight

print(max(dist))