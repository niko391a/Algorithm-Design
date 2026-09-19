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
        leftCandidate = ClosestPair(remainingPoints[0:pointsSplit])
        # Right half
        rightCandidate = ClosestPair(remainingPoints[pointsSplit:len(remainingPoints)])

        leftLength = EuclideanDistance(leftCandidate[0], leftCandidate[1])
        rightLength = EuclideanDistance(rightCandidate[0], rightCandidate[1])
        bestCandidate = leftCandidate if leftLength < rightLength else rightCandidate

        # Combine
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
                    currentDistance = EuclideanDistance(currentP1, currentP2)
                    if currentDistance < branchLength: 
                        branchCandidates = (currentP1, currentP2)
                        branchLength = currentDistance
        return branchCandidates

def EuclideanDistance(p1, p2):
    return math.sqrt(math.pow((p2[0]-p1[0]), 2) + math.pow((p2[1]-p1[1]), 2))



print(ClosestPair(points))