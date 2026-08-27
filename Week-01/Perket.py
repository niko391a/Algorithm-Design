# Thanks to RALC for pointing me to itertools and giving an example
    
import itertools


N = input()
combinations = []
ingredients = []

for x in range(n):
    ingredients[x] = tuple(input.split(" "))

for r in range(1, len(ingredients) +1):
    combinations.extend(itertools.combinations(ingredients, r))
print (combinations)