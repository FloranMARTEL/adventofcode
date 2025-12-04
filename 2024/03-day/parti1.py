#parti1
import re


file = open("inputExemple1.txt","r")
#file = open("input.txt","r")
data = file.read()



print("--")
a = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',data)
sum = 0
for i in a:
    sum += int(i[0]) * int(i[1])




print(sum)