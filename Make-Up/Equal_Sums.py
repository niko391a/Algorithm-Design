# Approach based on my KSALDES1KU study notes for Exhaustive Search.

def FindEqualSums(S):
    N = len(S)
    # sum -> first subset with that sum
    seen_sums = {}
    # skip mask 0 (empty set)
    for subset_mask in range(1, 1 << N):
        # bit i ON -> S[i] is in the subset
        subset = [S[i] for i in range(N) if subset_mask >> i & 1]
        current_sum = sum(subset)
        if current_sum in seen_sums:
            return seen_sums[current_sum], subset
        seen_sums[current_sum] = subset
    # all sums distinct -> Impossible
    return None


number_of_test_cases =  int(input())

for i in range(1, number_of_test_cases + 1):
    print(f"Case #{i}:")

    nums = list(map(int, input().split()))[1:]
    res = FindEqualSums(nums)


    if res == None:
        print("Impossible")
    else: 
        for sb in res:
            print(*sb)