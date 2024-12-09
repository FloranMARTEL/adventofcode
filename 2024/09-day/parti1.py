#parti1

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


print(stock)


i = 0
while i < len(stock):

    if stock[i] == None:
        j = len(stock)-1
        while stock[j] == None:
            del stock[j]
            j-=1

        stock[i] = stock[j]
        del stock[j]

    i+=1

print(stock)

s = 0

for i,v in enumerate(stock):
    s += i*v

print(s)
