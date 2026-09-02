N, t = map(int, input().split())
numList = list(map(int, input().split()))

match t:
    case 1:
        print("7")
    case 2:
        if numList[0] > numList[1]:
            print("Bigger")
        elif numList[0] == numList[1]:
            print("Equal")
        else:
            print("Smaller")
    case 3:
        numList.sort()
        size = len(numList)
        midVal = numList[size // 2]

        if numList.count(midVal) > size // 2: print(midVal)
        else: print(-1)

    case 4:
        numList.sort()
        size = len(numList)
        if size % 2 == 0:
            print(numList[size // 2], numList[size // 2 - 1])
        else:
            print(numList[size // 2 - 1])

    case 5:
        filteredList = list(filter(lambda x: 100 <= x <= 999, numList))
        filteredList.sort()
        print(*filteredList)

