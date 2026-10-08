# Augmenting path pseudo code from slides:
# AUGMENT(f, c, P)
#   b := bottleneck capacity of path P
#   foreach edge e ∈ P
#     if e ∈ E: f[e] := f[e] + b
#     else:     f[e^reverse] := f[e^reverse] - b
#   return f

n, m, s, t = map(int, input().split())

# List of edges:
# u = start 
# v = til 
# c = capacity 
# f = flow
edges = []

# Collection holding a list of vertices and their outgoing edges
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v, c, f = map(int, input().split())

    adj[u].append(v)

    edges.append([([u].append(v)), (c-f)])

