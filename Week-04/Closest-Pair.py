import math
import sys

points = []
n = int(sys.stdin.readline())
points = [tuple(map(float, sys.stdin.readline().split())) for _ in range(n)]

# Sort by x
points.sort()

# Find closest pair
def ClosestPair(remainingPoints):
    if len(remainingPoints) >= 4:
        # Split and recurse
        pointsSplit = len(remainingPoints)//2
        # Left half
        leftCandidate = ClosestPair(remainingPoints[:pointsSplit])
        # Right half
        rightCandidate = ClosestPair(remainingPoints[pointsSplit:])

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

        best = leftCandidate if leftLength < rightLength else rightCandidate

        for i in range(len(filteredPoints)):
            for j in range(i + 1, min(i + 12, len(filteredPoints))):
                if filteredPoints[j][1] - filteredPoints[i][1] >= delta:
                    break
                d = math.dist(filteredPoints[i], filteredPoints[j])
                if d < delta:
                    delta = d  
                    best = (filteredPoints[i], filteredPoints[j])
        return best
    else:
        # Base case
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

bestPair = ClosestPair(points)
for p in bestPair:
    print(*p)