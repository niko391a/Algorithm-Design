testCases = int(input())

for _ in range(testCases):
    workTrips = int(input())
    mySet = set()

    for _ in range(workTrips):
        currentCity = input()
        mySet.add(currentCity)

    print(len(mySet))
    