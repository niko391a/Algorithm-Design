x = list(input())
alternate = True

for i in range(len(x)):
    if x[i] == 'b':
        if alternate:
            x[i] = '0'
        else:
            x[i] = '1'
        alternate = not alternate

print("".join(x))