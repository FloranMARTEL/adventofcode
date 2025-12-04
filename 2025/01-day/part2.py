#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


def nbmoin(val,mod):
    cc = val
    cp = 0

    if val > 0:

        while cc >= mod:
            cc -=mod 
            cp+=1
        
        if cc == 0:
            cp-=1

    elif val < 0:
        while cc < 0:
            cc += mod 
            cp+=1
        
        # if cc ==0:
        #     cp+=1
    

    return cp

def m2(val,mod,curo):

    if val == 0:
        return 1

    

    cp = 0

    if val < 0 and curo == 0:
        cp -=1

    while val < 0 or val >=mod:

        if val < 0:
            val += mod

        elif val >= mod:
            val -= mod
        cp += 1

    # if val == 0:
    #     cp += 1
    
    return cp

def posval(val):
    cp = 0
    while val < 0:
        val += 100
        cp += 1
    
    return val,cp

mol = list(range(0,99+1))
print(mol)

dir = {
    "L":-1,
    "R" : 1
}

cur = 50

cpt = 0
for l in datalist:

    curo = cur

    num = l[1:]
    co = dir[l[0]]

    aid = int(num) // 100
    num = int(num) % 100
    num = str(num)

    val = int(num)*co

    cur += val


    nbm = m2(cur,100,curo)

    cpt+=aid
    cpt+=nbm

    if nbm > 1 :
        print("cc")
    

    cur = cur % 100



print(cur)
print(cpt)
# print(cpt2)