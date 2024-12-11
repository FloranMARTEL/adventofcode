#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split(" ")


def plus5(v):
    li = [v]
    a=5
    while a > 0:
        j = 0
        while j < len(li):
            if li[j] in dicp:
                val = dicp[li[j]]
                ll = len(val)
                if ll >= 5:
                    a = reversed(val[4])
                else:
                    a = 
                
                del datalist[j]
                for val in a:
                    li.insert(j,val)



            if li[j] == "0":
                li[j] = "1"
            elif len(li[j])%2 == 0:
                p = li[j]
                p1 = p[:len(p)//2]
                p2 = p[len(p)//2:]
                p2 = str(int(p2))

                del li[j]
                li.insert(j,p2)
                li.insert(j,p1)
                j+=1
            else:
                li[j] = str(int(li[j]) * 2024)
            
            j+=1

        a-=1
    return li

def nextval(val):
    li = [val]
    if li[j] == "0":
        li[j] = "1"
    elif len(li[j])%2 == 0:
        p = li[j]
        p1 = p[:len(p)//2]
        p2 = p[len(p)//2:]
        p2 = str(int(p2))

        del li[j]
        li.insert(j,p2)
        li.insert(j,p1)
        j+=1
    else:
        li[j] = str(int(li[j]) * 2024)
    
    return li

def calcul(li,nb,old = None):
    i = 0
    nv = []
    while i < len(li):

        nv.append(nextval(li[i]))

        i+=1

    calcul(nv,nb-1,li)

    if val in dicp:
        l = dicp[val]
        step = len(l)

        vl = []
        for v in l:
            vl.extend(calcul(v,nb-step-1))
        
        dicp[val].append()

    else:
        
        l = nextval(val)
        dicp[val] = [l]
        
        vl = []
        for v in l:
            vl.extend(calcul(v,nb-1))
    

    return vl
        





dicp = dict()

v = calcul(datalist,75)
        




print(len(v))