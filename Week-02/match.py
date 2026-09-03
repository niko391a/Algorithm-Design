# Thank you to RALC for suggesting a set of remaining suitors(proposers)

N, m = map(int, input().split())

proposers = {} 
rejectors = {}
proposer_partners = {}
rejector_partners = {}

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

    # if empty rejector has no partner
    if rejector_partners.get(currentPref) == []:
        proposer_partners[currentProposer] = currentPref
    # if rejector already has partner
    else:
        # rejector has a Better partner
        matches[currentProposer] = currentPref
        unmatched.add(currentProposer)

        # rejector has a worse partner
        partner = matches[currentProposer]



