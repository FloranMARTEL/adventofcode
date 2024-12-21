#parti1

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


paver = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None,"0","A"]
]

directione = [
    [None,"^","A"],
    ["<","v",">"]
]


rob1 = (3,2)
rob2 = (0,2)
rob3 = (0,2)


def findindex(man,c):
    for i in range(len(man)):
        for j in range(len(man[i])):
            if man[i][j] == c:
                return (i,j)

def convarr(dir,dic):

    text = ""
    if dir < 0:
        text += "^"*abs(dir)
    elif dir > 0:
        text += "v"*abs(dir)
    
    if dic < 0:
        text += "<"*abs(dic)
    elif dic > 0:
        text += ">"*abs(dic)
    

    return text+"A"

    
#'v<<A^>>AvA^A""v<<""A^>>AAv<A<A^>>AA<Av>AA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A'
#'<A>A""<""AAv<AA^>>AvAA^Av<AAA^>A'
def givepathr1(l,pav,rb):
    fin = ""
    for c in l:

        pasc = findindex(pav,c)

        dir = pasc[0] - rb[0]
        dic = pasc[1] - rb[1]

        ar = convarr(dir,dic)
        fin +=ar
        rb = pasc
    
    return fin,rb

su = 0
fin = ""
for l in datalist:
    newl,rob1 = givepathr1(l,paver,rob1)
    newl,rob2 = givepathr1(newl,directione,rob2)
    newl,rob3 = givepathr1(newl,directione,rob3)

    print(len(newl))
    su += (int(l[:-1]) * len(newl))

print(su)