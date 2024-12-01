#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")
l1 = [None] * len(datalist)
l2 = l1[:]

for i in range(len(datalist)):
    dd = datalist[i].split("   ")
    l1[i] = int(dd[0])
    l2[i] = int(dd[1])


l1.sort()
l2.sort()

diff = 0

for i in range(len(l1)):
    diff += abs(l1[i]-l2[i])


print(diff)
