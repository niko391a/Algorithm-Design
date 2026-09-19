import math

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
        branchCandidate = 0
        for p1 in range(len(remainingPoints)):
            for p2 in range(len(remainingPoints)):
            euclideanDistane = math.sqrt(math.pow((p2[0]-p1[0]), 2) + math.pow((p2[1]-p1[1]), 2))    

}

print(closestPair)