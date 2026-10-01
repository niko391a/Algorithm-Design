n, m = map(int, input().split())

nodes = []

for _ in range(n):
    node = tuple(map(int, input().split()))
    nodes.append(node)
    # Form (from, to, weight)

for node in nodes:
    