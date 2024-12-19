#parti2

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
        return 1
    if len(ini) > len(obj):
        return False

    res = 0
    for s in myset:
        if obj.startswith(ini+s):
            res = res + check(ini+s,obj)
    
    return res

cpt = 0
i = 0
for o in obj:
    print(i)
    i+=1
    cpt += check("",o)

print(cpt)