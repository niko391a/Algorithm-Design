x = list(input())
q = []

for i in range(len(x)):
    if x[i] == '<':
        y = q.pop()
        print("Popped: " + str(y))
    else: 
        q.append(x[i])
        print("Pushed: " + x[i])

print("".join(q))