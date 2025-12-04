#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

d = None
f = None

su = 0
for l in datalist:

    t = [None,None]
    for c in l:

        if c.isnumeric():
            t[1] = c

            if t[0] == None:
                t[0] = c
    
    chi = int(t[0]+t[1])
    su += chi

print(su)


