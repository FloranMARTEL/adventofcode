#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


input = datalist[0].split("\n")

diinput = dict()

for i in input:

    res  = i.split(" ")

    v = res[0].replace(":","")

    diinput[v] = int(res[1])

action = []
for a in datalist[1].split("\n"):

    a = a.split(" ")
    action.append((a[0],a[1],a[2],a[4]))



dicres = dict()

i = 0
while True:
    a = action[i]

    res = 0
    if a[0] in diinput and  a[2] in diinput:
        x = diinput[a[0]]
        y = diinput[a[2]]

        if a[1] == "AND":
            res = diinput[a[0]] & diinput[a[2]]

        elif a[1] == "OR":
            res = diinput[a[0]] | diinput[a[2]]
        elif a[1] == "XOR":
            res = diinput[a[0]] ^ diinput[a[2]]


        diinput[a[3]] = res

        del action[i]
    
    i+=1

    if len(action) == 0:
        break

    if i >= len(action):
        i = 0
    


reslist = []

for key in diinput:
    if key.startswith("z"):
        reslist.append((key,diinput[key]))


reslist.sort(key=lambda x : x[0],reverse=True)

bit = ""
for r in reslist:
    bit += str(r[1])

print(int(bit,2))

