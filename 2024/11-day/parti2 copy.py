#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split(" ")



def nextval(val):
    if val == "0":
        return ["1"]
    elif len(val)%2 == 0:
        p = val
        p1 = p[:len(p)//2]
        p2 = p[len(p)//2:]
        p2 = str(int(p2))

        return [p1,p2]

    else:
        return [str(int(val) * 2024)]
    





dicp = dict()
i = 75
while i > 0:
    print(i)
    j = 0
    while j < len(datalist):
        if datalist[j] in dicp:
            l = dicp[datalist[j]]

            del datalist[j]
            for v in reversed(l):
                datalist.insert(j,v)
        else:
            l = nextval(datalist[j])
            dicp[datalist[j]] = l

            del datalist[j]
            for v in reversed(l):
                datalist.insert(j,v)

        j+=len(l)


    i-=1


print(len(datalist))