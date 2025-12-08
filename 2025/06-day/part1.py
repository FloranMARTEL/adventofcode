#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

d = []
for ii,l in enumerate(datalist):

    ll = l.split(" ")

    for i in range(len(ll)-1,-1,-1):
        if ll[i] == "":
            del ll[i]


    if ii != len(datalist)-1:
        d.append(list(map(int,ll)))
    else:
        d.append(ll)


def mul(a,b):
    return a*b
def plu(a,b):
    return a+b

su =0 
for c in range(len(d[0])):

    op = None
    if d[-1][c] == "*":
        op = mul

        cal = 1

    else:
        op = plu
        cal = 0


    for l in range(len(d)-1):
        cal = op(cal,d[l][c])
    
    su += cal

print(su)



