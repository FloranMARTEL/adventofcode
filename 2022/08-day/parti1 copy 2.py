from copy import deepcopy

f = open("inputExemple.txt","r")

#f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

d2 = []

for i in range(len(datalist)):
    d2.append([])
    for j in range(len(datalist[i])):
        d2[i].append(int(datalist[i][j]))


d3 = deepcopy(d2)

i = 0
j = 0
k = len(d2)-1
l = len(d2[0])-1

while i != k:

    for x in range(len(d2)):
        for y in range(len(d2)):
            if ((x == i or x == k) or (y==j or y ==l)) and i-1< x < k+1 and j-1 < y < l+1 :

                if i == 0:
                    d3[x][y] = True
                else:

                    for a in [1,-1]:
                        
                            
                            c = 1

                            if d2[x+a][y] < d2[x][y]:

                                ok = True
                                while -1 < c*a + x < len(d2):
                                    if d3[c*a + x][y] == False:
                                        ok = False
                                        break
                                    c+=1
                                
                                if ok:
                                    d3[x][y] = True
                        
                    for b in [1,-1]:    
                        c = 1
                        
                        if d2[x][y+b] < d2[x][y]:

                            ok = True
                            while -1 < y+b*c < len(d2[0]):
                                if d3[x][y+b*c] == False:
                                    ok = False
                                    break
                                c+=1
                            
                            if ok:
                                d3[x][y] = True


    
    i+=1
    k-=1
    j+=1
    l-=1



cpt = 0
for l in d3:
    for e in l:
        if e==True:
            cpt+=1

print(cpt) 
            

