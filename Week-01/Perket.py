# Thanks to RALC for pointing me to itertools and giving an example
    
import itertools
import sys


bestAbsolute = sys.maxsize
N = int(input())

combinations = []
ingredients = []
prodSour = 1
sumBitter = 0

# get all ingredients into collection of tuples
for _ in range(N):
    s, b = map(int, input().split())
    ingredients.append((s, b))

# get all combinations
for r in range(1, len(ingredients) +1):
    combinations.extend(itertools.combinations(ingredients, r))

# evaluate collection of combinations and find best absolute difference
for combination in combinations:
    prodSour = 1
    sumBitter = 0

    for s, b in combination:
        prodSour *= s
        sumBitter += b

    difference = abs(prodSour - sumBitter)
    if difference < bestAbsolute: bestAbsolute = difference

print(bestAbsolute)
