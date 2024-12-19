#parti1

from  functools import *

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


myset = datalist[0].split(",")

myset = list(map(lambda x : x.replace(" ",""),myset))

obj = datalist[1].split("\n")

print(obj)

@cache
def check(ini, obj):
    if ini == obj:
        return True
    if len(ini) > len(obj):
        return False

    res = False
    for s in myset:
        if obj.startswith(ini+s):
            res = res or check(ini+s,obj)
    
    return res

cpt = 0
i = 0
for o in obj:
    print(i)
    i+=1
    if check("",o):
        cpt +=1

print(cpt)


