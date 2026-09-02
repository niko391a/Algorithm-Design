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
        print(numList[1])
    case 4:
        print(sum(numList))
    case 5:
        evenSum = 0
        for n in numList:
            if n % 2 == 0:
                evenSum += n
    case 6:
        modList = list

        for n in numList:
            modList.append(n%23)

            print("".join(modList))
    case 7:
        i = numList[0]
    
        while True:
            if(i >= len(numList)):
                print("Out")
            elif(i == len(numList)-1):
                print("Done")
            elif

