import sys
import random
import time

if len(sys.argv) == 1:
    start = time.time()
    N = int(input())
    weights = []

    #python3 lecture.py < 1.in

    # The assumptions is that the start and end times are already sorted
    for i in range(N):
        a, b, w = map(int, input().split())
        # Asserts are to ensure that programs fail early
        assert a == i # ensure that a is my index
        assert b == a+2 # 
        assert w >= 0 # ensure the value is non-negative

        weights.append(w)
else:
    N = int(sys.argv[1])
    weights = list(random.randrange(1, 100) for _ in range(N))
    
# Terrible from an engineering standpoint (global vars)
memo = dict()

def solve(i):
    if i == 0:
        return 0

    if i == 1:
        return weights[0]

    if i not in memo : # save computation for already computed steps
        take = weights[i-1] + solve(i-2) # taking the last job we care about [i-1]
        leave = solve(i-1)
        memo[i] = max(take, leave)
    return memo[i]

sol = solve(N)

print(f"{N} {time.time()-start} {sol}")