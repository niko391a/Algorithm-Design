# Thanks to RALC for pointing me to itertools and giving an example
    
import itertools
import sys


bestAbsolute = sys.maxsize
N = input()
combinations = []
ingredients = []
prodSour = 0
sumBitter = 0

# Get all ingredients into collection of tuples
for x in range(N):
    ingredients[x] = tuple(input.split(" "))

# Get all combinations
for r in range(1, len(ingredients) +1):
    combinations.extend(itertools.combinations(ingredients, r))

# Evaluate collection of combinations and find best absolute difference
for combination in combinations:
    prodSour *= combination[1]
    sumBitter += combination[1]
    difference = prodSour - sumBitter
    if difference < bestAbsolute: bestAbsolute = difference
