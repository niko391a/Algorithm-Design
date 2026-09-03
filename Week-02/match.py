# Thank you to RALC for suggesting a set of remaining suitors(proposers)

N, m = map(int, input().split())

proposers = {} 
rejectors = {}
matches = {}

# Proposors
for _ in range(N // 2):
    parts = input().split()
    name = parts[0]
    proposers[name] = parts[1:]

# Rejectors
for _ in range(N // 2):
    parts = input().split()
    name = parts[0]
    rejectors[name] = parts[1:]

unmatched = set(proposers)

# Pair sim
while len(unmatched) != 0:
    currentProposer = unmatched.pop()
    currentPref = proposers[currentProposer].pop(0)

    # if empty no partner
    if matches[currentProposer] == []:
        matches[currentProposer] = currentPref
    # if has partner
    else:
        # Better partner
        matches[currentProposer] = currentPref
        
        # Worse partner




