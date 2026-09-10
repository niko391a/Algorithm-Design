# Thank you to KAJN for reminding me how to split inputs into tuples

n = int(input())

intervals = []
optimalSet = []

for _ in range(n):
    interval = tuple(map(int, input().split()))
    intervals.append(interval)

# Sort by end time
intervals.sort(key=lambda x: x[1])

# We know the first element must be in the optimal set
optimalSet.append(intervals[0])
PrevOptimalEnd = intervals[0][1]

for i in range(1, n):
    if intervals[i][0] >= PrevOptimalEnd:
        optimalSet.append(intervals[i])
        PrevOptimalEnd = intervals[i][1]

print(len(optimalSet))        