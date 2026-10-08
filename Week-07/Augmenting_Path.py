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
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v, c, f = map(int, input().split())
    if f < c:                       # forward edge exists: spare capacity c - f
        adj[u].append((v, c - f))
    if f > 0:                       # backward edge exists: flow that can be undone
        adj[v].append((u, f))       # goes into v's list, pointing back to u


# BFS to find the bottleneck
