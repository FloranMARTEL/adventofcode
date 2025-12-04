#parti2

from  functools import *

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

@cache
def cn(l,i,v,n):

    if n == 0:
        global max
        if max == None or max < int(v):
                max = int(v) 
        return

    v2max = None
    for j in range(i+1,len(l)-(n-1)):
        v2 = int(l[j])

        if v2max == None or v2 > v2max:
            v2max = v2
            nv = v+str(v2)
            
            nv += "9" * (12 - len(nv))

            if max != None and int(nv) < max:
                 return
            
            

            cn(l,j,nv,n-1)
    

su = 0
for l in datalist:
    max = None

def mymax(l,i,j):
    max = None
    index = None
    for i in range(i,j):
        if max == None or max < l[i]:
            max = l[i]
            index = i
    
    return max,index


def cn(l,i,n):

    if n == 0:
        return ""
    
    m,id = mymax(l,i+1,len(l)-(n-1))        

    return str(m)+cn(l,id,n-1)


su = 0
for l in datalist:

    l2 = map(int,l)

    v = cn(l,-1,12)

    su += int(v)
    print(v)


print("su : ",su )
    



    cn(l,-1,"",12)
                        
    print(max)
    su += max

print(su)
        

