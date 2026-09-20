import math

n = int(input())

points = []

for _ in range(n):
    point = tuple(map(float, input().split()))
    points.append(point)

# Sort by x
points.sort()

# Find closest pair
def ClosestPair(remainingPoints):
    if len(remainingPoints) >= 4:
        # Split and recurse
        pointsSplit = len(remainingPoints)//2
        # Left half
        leftCandidate = ClosestPair(remainingPoints[pointsSplit-1])
        # Right half
        rightCandidate = ClosestPair(remainingPoints[pointsSplit])

        # Combine
        leftLength = math.dist(leftCandidate[0], leftCandidate[1])
        rightLength = math.dist(rightCandidate[0], rightCandidate[1])

        delta = min(leftLength, rightLength)
        line =  remainingPoints[pointsSplit][0]
        filteredPoints = []

        for p in remainingPoints:
            if (abs(p[0] - line)) < delta:
                filteredPoints.append(p)

        filteredPoints.sort(key=lambda x: x[1])

        return leftCandidate if leftLength < rightLength else rightCandidate

    else:
        # Base case evaluate the 9 pairs no clean split for 3 points
        branchLength = math.inf
        branchCandidates = []
        currentP1 = []
        currentP2 = []
        currentDistance = 0

        for p1 in range(len(remainingPoints)):
            currentP1 = remainingPoints[p1]
            for p2 in range(len(remainingPoints)):
                if p1 != p2:
                    currentP2 = remainingPoints[p2]
                    currentDistance = math.dist(currentP1, currentP2)
                    if currentDistance < branchLength: 
                        branchCandidates = (currentP1, currentP2)
                        branchLength = currentDistance
        return branchCandidates

print(ClosestPair(points))