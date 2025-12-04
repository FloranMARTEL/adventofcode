#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


su = 0
for l in datalist:
    max = None 
    v1f = None
    for i in range(len(l)-1):

        v1 = int(l[i])

        if v1f == None or v1 > v1f:
            v1f = v1
            
            v2max = None
            for j in range(i+1,len(l)):
                v2 = int(l[j])

                if v2max == None or v2 > v2max:
                    v2max = v2
            

            nu = int(str(v1f)+str(v2max))
            if max == None or max < nu:
                max = nu 
                        
    print(max)
    su += max

print(su)
        

