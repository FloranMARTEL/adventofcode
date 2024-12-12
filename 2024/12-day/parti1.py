#parti1

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")



region = []

dire = [(-1,0),(-1,-1),(0,-1),(-1,1)]

for i in range(len(datalist)):
    for j in range(len(datalist[i])):

        tro = False

        for r in range(len(region)):
            for d in dire:
                if i+d[0] >= 0 and i+d[0] < len(datalist) and j+d[1] >= 0 and j+d[1] < len(datalist[0]):
                    if (i+d[0],j+d[1],datalist[i][j]) in region[r]:
                        region[r].add((i,j,datalist[i][j]))
                        tro = True
                        break
            
            if tro:
                break
        
        if tro == False:
            s = set()
            s.add((i,j,datalist[i][j]))
            region.append(s)

    
print(region)
print(len(region))

for r in region:
    if len(r) == 1:
        print(r)

        


        