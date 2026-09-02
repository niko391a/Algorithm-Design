x = list(input())
out = ""
alternate = True

for c in x:
    if c == 'b':
        if alternate:
            out = out+"1"
        else:
            out = out+"0"
    else: 
        out = out + c

    alternate = not alternate
print(out)