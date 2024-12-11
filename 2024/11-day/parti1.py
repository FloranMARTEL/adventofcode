#parti1

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
data = file.read()

datalist = data.split(" ")




i = 25
while i > 0:

    for j in range(len(datalist)):
        if datalist[j] == "0":
            datalist[j] = "1"
        elif len(datalist[j])%2 == 0:
            p = datalist[j]
            p1 = p[len(p)//2]
            p2 = p[len(p)//2:]
            p2 = str(int(p2))

            del datalist[j]
            datalist.insert(j,p2)
            datalist.insert(j,p1)
        else:
            datalist[j] = str(int(datalist[j]) * 2024)

    i-=1


datalist = list(map(int,datalist))

print(sum(datalist))