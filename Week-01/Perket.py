# Thanks to RALC for pointing me to itertools and giving an example
    
import itertools
import sys


bestAbsolute = sys.maxsize
N = input()
combinations = []
ingredients = []

# Get all ingredients into collection of tuples
for x in range(n):
    ingredients[x] = tuple(input.split(" "))

# Get all combinations
for r in range(1, len(ingredients) +1):
    combinations.extend(itertools.combinations(ingredients, r))

# Evaluate collection of combinations and find best absolute difference

