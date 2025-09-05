

f = open("inputExemple.txt","r")

# f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

i = 1
X = 1

s = 0
for gdataligne in datalist:
    ligne = gdataligne.split(" ")

    instu = ligne[0]

    if instu == "noop":
        pass
    elif instu == "addx":
        i+=1
        if (i-20)%40 == 0:
            print("add",X,(i))
            s += X*(i) 
        val = int(ligne[1])
        X += val

    i += 1

    if (i-20)%40 == 0:
        print("add",X,(i))
        s += X*(i)


print(s)
    # instru, val = ligne[0], ligne[1]
    # print(instru, val)
print((60-20)%40)