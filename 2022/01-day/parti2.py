

d  = {
    "A" : "a",
    "X" : "a",
    "B" : "b",
    "Y" : "b",
    "C" : "c",
    "Z" : "c"
}


dd = {
    "AL" : "c",
    "AW" : "b",
    "BW" : "c",
    "BL" : "a",
    "CW" : "a",
    "CL" : "b",
}


pc = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

pr = {
    "W" : 6,
    "L" : 0,
    "N" : 3
}


data = open("inputExemple.txt","r").read()


f = open("input.txt","r")
data = f.read()

ldata = data.split("\n")

totalScore = 0
for da in ldata:
    a = d[da[0]]
    
    score : int = 0
    if da[2] == "X":
        b = dd[da[0]+"L"]
    elif da[2] == "Z":
        b = dd[da[0]+"W"]
        score = 6
    else:
        b = a
        score = 3
    
    score += pc[b]

    print(score)


    totalScore+=score

print(totalScore)