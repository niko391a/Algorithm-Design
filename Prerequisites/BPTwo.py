N = input
t = input
numList = list

for x in range(N):
    numList.append(x)

match t:
    case 1:
        lucky = False
        numSet = numList
        for num in numSet:
            complement = 7777-num
            if complement in numSet: lucky = True
        if lucky: print("Yes") 
        else: print("No")
    case 2:
        numSet = numList
        if len(numSet) != len(numList):
            print("Contains duplicates")
        else:
            print("Unique")
    case 3:
        numList.sort
        size = len(numList)
        if numList[size/2] == numList[0]: print(numList[0])
        else: print(-1)
    case 4:
        numList.sort
        size = len(numList)
        if size % 2 == 0:
            print(numList[size] + " ")
            print(numList[size-1])
        else:
            print(numList[size-1])
    case 5:
        filteredList = list(filter(lambda x: x < 100 or x > 999, numList))
        filteredList.sort
        for num in filteredList:
            print(num + " ")

