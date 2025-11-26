#parti1
from functools import *
file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

datalist = list(map(int,datalist))

@cache
def caval(d):
    mul1 = d * 64
    d = (d ^ mul1)%mod

    div1 = d // 32
    d = (d ^ div1)%mod

    mult2 = d * 2048
    d = (d^mult2)%mod

    return d

mod = 16777216
ma = 0
li = None

dic = dict()
su = 0
for d in datalist:
    q = (None,None,None,None)
    oldd = None 
    view = set()
    for i in range(2000):
        
        d = caval(d)

        if oldd == None:
            oldd = d%10
        else:
            dif = (d%10)-oldd
            oldd = d%10
            q = (q[1],q[2],q[3],dif)

        if i > 3:
            if q not in view:

                if q not in dic:
                    dic[q] = (d%10)
                else:
                    dic[q] += (d%10)
            view.add(q)
    
    
m  = None

for key in dic:

    if m== None or dic[key] > dic[m]:
        m = key

print(m,dic[m])