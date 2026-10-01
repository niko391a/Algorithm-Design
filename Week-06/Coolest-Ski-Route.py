n, m = map(int, input().split())

graph = []

for _ in range(n):
    node = tuple(map(int, input().split()))
    nodes.append(node)
    # Form (from, to, weight)

for _ in range(m):
    for node in graph:
        for u, v, weight in graph[node].items():
            if 