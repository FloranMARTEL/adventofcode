#parti1
from functools import *
file = open("inputExemple.txt","r")
# file = open("input.txt","r")
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
import queue

for i in range(-9,9):
    for j in range(-9,9):
        if abs(i+j) > 9 :
            continue
        for k in range(-9,9):
            if abs(j+k) > 9 :
                continue
            for l in range(-9,9):
                if abs(k+l) > 9 :
                    continue
                ci = [i,j,k,l]

                su = 0
                for d in datalist:
                    q = queue.Queue(4)
                    oldd = None 
                    for i in range(2000):
                        if q.qsize() == 4:
                            q.get()
                        
                        d = caval(d)

                        if oldd == None:
                            oldd = d
                        else:
                            dif = (d%10)-oldd
                            oldd = d%10
                            q.put(dif)
                        
                        if q.qsize() == 4:
                            cj = [q.get(),q.get(),q.get(),q.get()]
                            if cj == ci:
                                break

                            for c in cj:
                                q.put(c)
                    
                    su += d
    
                if su > ma:
                    ma = su
                    li = ci

print(li)