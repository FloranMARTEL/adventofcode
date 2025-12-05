TCHITOVAL = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

Dir8 = [
    (1,0),
    (1,-1),
    (0,-1),
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,1),
    (1,1),
],


Dir4 = [
    (1,0),
    (0,-1),
    (-1,0),
    (0,1)
]

def gendir(i,j,dir):
    l = []
    for d in dir:
        newi = i+d[1]
        newj = j+d[0]
        l.append((newi,newj))

    return l

def inBorder(i,j,l):
    return i >= 0 and i < len(l) and j >= 0 and j < len(l[i])


