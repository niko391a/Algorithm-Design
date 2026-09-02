x = list(input())
q = []

for i in range(len(x)):
    if x[i] == '<':
        y = q.pop()
    else: 
        q.append(x[i])

print("".join(q))