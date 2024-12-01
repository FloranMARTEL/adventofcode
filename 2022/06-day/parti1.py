

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

space = 4-1
for i in range(space,len(data)):
    s = set(data[i-space:i+1])
    print(s)
    if len(s) == 4:
        break


print(i+1)