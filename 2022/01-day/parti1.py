

d  = {
    "A" : "a",
    "X" : "a",
    "B" : "b",
    "Y" : "b",
    "C" : "c",
    "Z" : "c"
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
    b = d[da[2]]
    
    score = pc[b]
    result = ""
    if a == b:
        result = "N"
    elif a == "c" and b == "a":
        result="W"
    elif a == "a" and b == "b":
        result="W"
    elif a == "b" and b == "c":
        result="W"
    else:
        result="L"

    score += pr[result]
    print(score)

    totalScore+=score

print(totalScore)