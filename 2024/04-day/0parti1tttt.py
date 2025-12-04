#parti1
import numpy as np
import re
from copy import deepcopy

file = open("inputExemple.txt","r")
#file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


from Matrix import *

m = Matrix(datalist)

print(m.get())
print(m.getVert())
print(m.getdiagDG())
print("--------------")
print(m.getdiagGD())
print("--------------")
print(m.getdiagGD().convLigneIntoString())
print(m)


