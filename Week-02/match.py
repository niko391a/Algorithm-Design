# Thank you to RALC for suggesting a set of remaining suitors(proposers) as well as using dictionaries for tracking current matches

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
    if rejector_partners.get(currentPref) == None:
        proposer_partners[currentProposer] = currentPref
        rejector_partners[currentPref] = currentProposer
    # if rejector already has partner
    else:
        # Compare partner to candidate
        currentPartner = rejector_partners[currentPref]
        new_is_preferred = False

        for candidate in rejectors[currentPref]:
            if candidate == currentProposer:
                new_is_preferred = True
                break
            if candidate == currentPartner:
                break

        # rejector has a worse partner
        if new_is_preferred:
            proposer_partners[currentProposer] = currentPref
            rejector_partners[currentPref] = currentProposer
            unmatched.add(currentPartner)
        # rejector has a Better partner return to unmatch
        else:
            unmatched.add(currentProposer)

for proposer, partner in proposer_partners.items():
    print(proposer, partner)



