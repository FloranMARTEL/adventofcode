#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


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

def mynum(t,i):

    for nu in TCHITOVAL:

        if i+len(nu) > len(t):
            continue

        if t[i:i+len(nu)] == nu:
            return str(TCHITOVAL[nu])
    
    return False


su = 0
for l in datalist:

    t = [None,None]
    for ii,c in enumerate(l):

        if c.isnumeric():
            t[1] = c

            if t[0] == None:
                t[0] = c
        
        v = mynum(l,ii)
        if v != False:
            t[1] = v

            if t[0] == None:
                t[0] = v

    
    chi = int(t[0]+t[1])
    su += chi

print(su)
