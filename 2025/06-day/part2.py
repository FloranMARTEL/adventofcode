#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


def conv(m):
    maxs = max(map(lambda x : len(str(x)),m))

    newv = [""]*maxs
    for l in range(len(m)-1,-1,-1):
        for c in range(len(str(m[l]))-1,-1,-1):
            newv[c] = str(m[l])[c]+newv[c]

    return list(map(int,newv))

dd = []
for ii,l in enumerate(datalist):

    ll = l.split(" ")

    for i in range(len(ll)-1,-1,-1):

        if ll[i] == "":
            del ll[i]

    dd.append(ll)

d = []
vc = 0
for cc in range(len(dd[0])):
    newd = []
    for l in range(len(dd)-1):
        newd.append(dd[l][cc])
    
    maxs = max(map(lambda x : len(str(x)),newd))
    curll = [[]]
    for c in range(maxs):
        for l in range(len(datalist)):
            if (not datalist[l][vc].isnumeric()) and l == len(datalist)-1:
                curll.append([])
                break

            curll[-1] += datalist[l][vc]
        
        vc+=1

    newcur = [""]*(len(curll)-1)
    for i in range(len(curll)-1):
        for v in curll[i]:
            if v != " ":
                newcur[i] += v
    
    newcur.append(dd[-1][cc])
    d.append(newcur)
    vc+=1



def mul(a,b):
    return a*b
def plu(a,b):
    return a+b





su =0 

for l in range(len(d)):
    op = None
    if d[l][-1] == "*":
        op = mul

        cal = 1

    else:
        op = plu
        cal = 0

    
    for c in range(len(d[l])-1):
        cal = op(cal,int(d[l][c]))

    print(cal)
    su += cal

    
    

print(su)



