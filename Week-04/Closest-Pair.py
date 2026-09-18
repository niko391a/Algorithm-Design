n = int(input())

points = []
closestPair = []

for _ in range(n):
    point = tuple(map(float, input().split()))
    points.append(point)

# Sort by x
points.sort(key=lambda x: x[1])

# Find closest pair

print(closestPair)