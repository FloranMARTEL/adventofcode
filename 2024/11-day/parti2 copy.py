#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split(" ")


class Rock:
    
    def __init__(self,val,compte):
        self.compte = compte
        self.val = val
        self.child = []

    # def next()
    


        




for v in range(len(datalist)):
    datalist[v] = (datalist[v],1)



i = 75
while i > 0:
    cpt = dict()

    for v in datalist:
        if v[0] in cpt:
            cpt[v[0]] += v[1]
        else:
            cpt[v[0]] = v[1]

    l = []
    for key in cpt:
        
        if key == "0":
            l.append(("1",cpt[key]))
        elif len(key)%2 == 0:

            l.append((key[:len(key)//2],cpt[key]))
            l.append((str(int(key[len(key)//2:])),cpt[key]))
        else:
            l.append((str(int(key)*2024),cpt[key]))


    datalist = l
    i -= 1





        
s=0
for v in datalist:
    s+=v[1]

print(s)