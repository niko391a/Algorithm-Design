# Thank you to KAJN for reminding me of abs() for the condition

N = int(input())

weights = []

for i in range(N):
    w = int(input())
    assert w >= 0 # ensure the value is non-negative
    weights.append(w)

weightStack = {0}

# loop and for every new weight added i create new combinations 
# by computing the sums of the new weight and old combinations.

for w in weights:
    new_sums = set()
    for v in weightStack:
        if w+v <= 2000:
            new_sums.add(w+v)
    for v in new_sums:
        weightStack.add(v)

sol = 0;
best_dist = 1000

for w in weightStack:
    dist = abs(w - 1000)
    if dist < best_dist or (dist == best_dist and w > sol):
        sol = w
        best_dist = dist

print(sol)