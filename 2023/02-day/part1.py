#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

lim = {
    "blue" : 14,
    "green" : 13,
    "red" : 12
}
su = 0
for l in datalist:

    [p1,p2] = l.split(":")

    id = int(p1[5:])

    valid = True

    for g in p2.split(";"):

        p = g.split(",")
        for pi in p:
            
            [w,v,c] = pi.split(" ")

            v = int(v)

            if v > lim[c]:
                valid = False
    
    if valid == True:
        su += id
        print(id)


print(su)
            
