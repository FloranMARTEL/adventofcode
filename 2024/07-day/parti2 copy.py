#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

li = []
for i in range(len(datalist)):
    v = datalist[i].split(":")

    u = v[1].split(" ")[1:]
    u = list(map(int,u))

    li.append([int(v[0]),u])



def rec(val,test,cal,i=1):

    if cal > test:
        return (False,0)

    if len(val) == i:
        
        if cal == test:
            return (True,cal)
        else:
            return (False,0)
    
    newi = i+1
    
    (r1,s) = rec(val,test,cal+val[i],newi)

    if r1:
        return (r1,s)

    (r2,s2) = rec(val,test,cal*val[i],newi)

    if r2:
        return (r2,s2)
    

    (r3,s3) = rec(val,test,int(str(cal)+ str(val[i])),newi)

    if r3:
        return (r3,s3)
    

    return False,0

sum = 0
for l in li:
    print(l)

    (a,c) = rec(l[1],l[0],l[1][0])

    if a:
        sum += c

        

print(sum)



