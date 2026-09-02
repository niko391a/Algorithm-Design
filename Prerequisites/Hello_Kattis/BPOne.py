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
        print(evenSum)
    case 6:
        modString = []

        for n in numList:
            modString.append(chr((n%26) + 97))

        print("".join(modString))
    case 7:
        i = numList[0]
        prevI = set()

        while True:
            if(i >= len(numList)):
                print("Out")
                break
            elif(i == len(numList)-1 or i < 0):
                print("Done")
                break
            elif i in prevI:
                print("Cyclic")
                break
            prevI.add(i)
            i = numList[i]

