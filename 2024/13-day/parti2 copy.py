#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")

su = 0
for d in datalist:

    li = d.split("\n")
    
    a = li[0].split(":")[1].split(",")
    a = (int(a[0][3:]),int(a[1][3:]))

    b = li[1].split(":")[1].split(",")
    b = (int(b[0][3:]),int(b[1][3:]))


    p = li[2].split(":")[1].split(",")
    p = (10000000000000+int(p[0][3:]),10000000000000+int(p[1][3:]))
    #p = (int(p[0][3:]),int(p[1][3:]))


    prix = None
    curentpos = [0,0]
    
    coef = b[0] / b[1]

    print(22/67)
    o = a[1]*coef - a[0]
    print((34*coef)-94)
    k = (p[1]*coef - p[0])/o
    print((p[1]*coef - p[0])/o)


    j = (p[0]-(k*a[0]))/b[0]

    for eck in [-1,0,1]:
        for ecj in [-1,0,1]:

            newk = int(k) + eck
            newj = int(j) + ecj


            curentpos[0] = int(b[0]*newj + a[0]*newk)
            curentpos[1] = int(b[1]*newj + a[1]*newk)


            if curentpos[0] == p[0] and curentpos[1] == p[1] :
                su += (newk*3 + newj)        
    
            
            



            
    
    if prix != None:
        su += prix


print(su)