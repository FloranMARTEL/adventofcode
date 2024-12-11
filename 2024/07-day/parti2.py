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



def rec(val,operateur,test):


    if len(operateur) == len(val)-1:

        cal = val[0]

        for i in range(1,len(val)):
            
            if operateur[i-1] == "*":
                cal *= val[i]
            elif operateur[i-1] == "+":
                cal += val[i]
            elif operateur[i-1] == "||":
                p = str(cal)
                m = str(val[i])
                cal = int(p+m)
        
        if cal == test:
            return (True,cal)
        else:
            return (False,0)
    
    newop1 = operateur[:]
    newop1.append("+")
    (r1,s) = rec(val,newop1,test)


    if r1:
        return (r1,s)

    newop2 = operateur[:]
    newop2.append("*")
    (r2,s2)= rec(val,newop2,test)

    if r2:
        return (r2,s2)
    
    newop3 = operateur[:]
    newop3.append("||")
    (r3,s3)= rec(val,newop3,test)

    if r3:
        return (r3,s3)
    

    return False,0

sum = 0
for l in li:
    print(l)

    (a,c) = rec(l[1],[],l[0])

    if a:
        sum += c

        

print(sum)



