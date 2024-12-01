#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")
l1 = []
l2 = []

for i in range(len(datalist)):
    dd = datalist[i].split("   ")
    l1.append(int(dd[0]))
    l2.append(int(dd[1]))






l1.sort()
l2.sort()




print(l1)
print(l2)

diff = 0

for i in range(len(l1)):
    diff += abs(l1[i]-l2[i])
    #print(abs(l1[i]-l2[i]))

print(diff)
