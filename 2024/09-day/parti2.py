#parti2


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

# datalist = data.split("\n")

data = list(map(int,data))
stock = []
num = 0
for i in range(len(data)):

    if i%2 == 0:

        for j in range(data[i]):
            stock.append(num)
        num+=1
    
    else:
        for j in range(data[i]):
            stock.append(None)


j = len(stock)-1
while j >=0:
    print(j)
    if stock[j] == None:
        pass
    else:
        l = data[stock[j]*2]

        val = stock[j]
        if val == 2:
            print('ici')
        elif val == 7:
            print('ici')
        

        cpt = 0
        find = False
        for i in range(j):
            if stock[i] != None:
                cpt = 0
            else:
                cpt+=1
                if cpt == l:
                    find=True
                    break
            
        if find:
        
            for o in range(i,i-l,-1):
                stock[o] = val
            
            for o in range(j,j-l,-1):
                stock[o] = None
        else:
            j-=l-1

    j-=1
    


print(stock)

s = 0

for i,v in enumerate(stock):
    if v != None:
        s += i*v


print(s)

