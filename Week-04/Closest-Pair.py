n = int(input())

points = []

for _ in range(n):
    point = tuple(map(float, input().split()))
    points.append(point)

# Sort by x
points.sort()

# Find closest pair
def ClosestPair(bestCandidate, remainingPoints) {
    if len(remainingPoints) != 3:
        # Split and recurse
        ClosestPair(bestCandidate, remainingPoints.)

        # Combine
    else:
        # Base case evaluate the 9 pairs no clean split for 3 points

}

print(closestPair)