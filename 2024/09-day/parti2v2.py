#parti2


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

# datalist = data.split("\n")

data = list(map(int,data))

dd = [None]*(len(data)//2+1)

for i in range(0,len(data)//2+1,1):
    dd[i] = i


j = len(data)-1
while j >= 0:


    for i in range(1,j,2):
        if data[i] >= data[j]:
            val = data[j]
            data[i] -= val

            data.insert(i,val)
            data.insert(i,0)

            bnum = dd[j//2]
            dd.insert(i//2+1,bnum)

            if j+2+1 < len(data):
                data[j+2+1] += data[j+2] + data[j+2-1]
            del data[j+2]
            del data[j+2-1]

            del dd[j//2+1]
            j+=2
            break
    
    
    j-=2


stock = []
for i in range(len(data)):

    if i%2 == 0:

        for j in range(data[i]):
            stock.append(dd[i//2])
    
    else:
        for j in range(data[i]):
            stock.append(None)



s = 0

for i,v in enumerate(stock):
    if v != None:
        s += i*v


print(s)

