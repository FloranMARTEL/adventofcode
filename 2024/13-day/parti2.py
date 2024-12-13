#parti2

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
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


    prix = None
    curentpos = [0,0]
    k = p[0] // b[0]
    x = k//2
    l = 0
    while True:
        print(x)

        xb0 = b[0]*x
        xb1 = b[1]*x
        if xb0 > p[0] or xb1 > p[1]:
                break
        
        o = p[0]-xb0 // a[0]
        y = o//2
        m = 0
        while True:
            curentpos[0] = xb0 + a[0]*y
            curentpos[1] = xb1 + a[1]*y



            if curentpos[0] == p[0] and curentpos[1] == p[1] :
                newprix = x*1 + y*3

                if prix == None or newprix < prix:
                    prix = newprix 

                print(x,y)
                print(newprix)
                print("ok")
            
            elif curentpos[0] > p[0]:
                o = y
                newy = m+((o-m)//2)
                if newy == y:
                     break
                else:
                     y = newy
            elif curentpos[0] < p[0]:
                m = y
                newy = m+((o-m)//2)
                if newy == y:
                     break
                else:
                     y = newy
            else:
                 break
                 
            
        x+=1
            
            



            
    
    if prix != None:
        su += prix


print(su)