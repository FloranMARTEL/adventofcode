#parti1

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
    p = (int(p[0][3:]),int(p[1][3:]))


    prix = None
    curentpos = [0,0]
    for x in range(0,100):

        for y in range(0,100):
            
            # if y == 80 and x == 40:
            #     print("ici")

            curentpos[0] = b[0]*x + a[0]*y
            curentpos[1] = b[1]*x + a[1]*y

            if curentpos[0] == p[0] and curentpos[1] == p[1] :
                newprix = x*1 + y*3

                if prix == None or newprix < prix:
                    prix = newprix 

                print(x,y)
                print(newprix)
                print("ok")
    
    if prix != None:
        su += prix


print(su)



