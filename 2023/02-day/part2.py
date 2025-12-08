#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


su = 0
for l in datalist:
    lim = {
        "blue" : 0,
        "green" : 0,
        "red" : 0
    }

    [p1,p2] = l.split(":")

    id = int(p1[5:])


    for g in p2.split(";"):

        p = g.split(",")
        for pi in p:
            
            [w,v,c] = pi.split(" ")

            v = int(v)

            if v > lim[c]:
                lim[c] = v
    
    res = lim["blue"] * lim["green"] * lim["red"]
    su += res
    print(res)


print(su)
            
