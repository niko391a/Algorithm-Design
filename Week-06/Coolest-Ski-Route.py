# Credit to https://www.geeksforgeeks.org/dsa/bellman-ford-algorithm-simple-implementation/ for some inspiration.
# n(nodes) m(edges)
n, m = map(int, input().split())

graph = []
dist = []

for _ in range(m):
    edge = tuple(map(int, input().split()))
    graph.append(edge)
    # Form (from, to, weight)

for _ in range(m):
    for u, v, weight in graph:
        dist[v] = dist[u] + weight
        if