#parti2
import re

file = open("inputExemple2.txt","r")
#file = open("input.txt","r")
data = file.read()

#datalist = data.split("\n")
# sum = 0
# d = 0
# activation = True
# while d < len(data)-3:

#     if data[d:d+4] == "do()":
#         activation = True
    
#     s = data[d:d+7]
#     if data[d:d+7] == "don't()":
#         activation = False

#     v = data[d:d+12]
#     if data[d:d+4] == "mul(":
        
#         digit1 = ""
#         d = d+3
#         end = False
#         faux = False
#         for i in range(1,5):
#             a=data[d+i]

#             if data[d+i].isdigit() and i<4:
#                 digit1+=data[d+i]
            
#             elif data[d+i] == ',':
#                 end = True
#                 break
#             else:
#                 faux = True
#                 break
            
#         d = d+i
        
        
#         if (not faux) and not (len(digit1) == 0 or len(digit1) > 3):
#             digit2 = ""
#             end = False
#             faux = False

#             for i in range(1,5):
#                 a=data[d+i]

#                 if data[d+i].isdigit() and i<4:
#                     digit2+=data[d+i]
                
#                 elif data[d+i] == ')':
#                     end=True
#                     break
#                 else:
#                     faux = True

#                     break
                
#             #d = d+i

#             if (not faux) and not (len(digit2) == 0 or len(digit1) > 3) and activation:
#                 print(digit1,digit2)
#                 sum += int(digit1)*int(digit2)

    

#     d+=1

print("--")
a =[]
r = re.search(r'mul\((\d{1,3}),(\d{1,3})\)',data) 
while r != None:
    end = r.span(0)[1]
    a.append((r.span(0)[1],int(r.group(1))* int(r.group(2))))
    data = data[end:]
    r = re.search(r'mul\((\d{1,3}),(\d{1,3})\)',data)

b =[]
r = re.search(r'do\(\)',data) 
while r != None:
    end = r.span(0)[1]
    b.append(r.span(0)[1])
    data = data[end:]
    r = re.search(r'don\'t\(\)',data)

c =[]
r = re.search(r'don\'t\(\)',data) 
while r != None:
    end = r.span(0)[1]
    c.append(r.span(0)[1])
    data = data[end:]
    r = re.search(r'don\'t\(\)',data)



activate = True
sum = 0
i = 0
while i < len(a):

    if len(b) != 0 and b[0] < a[i][0] and b[0] < c[0]:
        activate = True
        del b[0]
    elif len(c) != 0 and c[0] < a[i][0] and c[0] < b[0]:
        activate = False
        del c[0]

    elif activate:
        sum += a[i][1]
        i+=1
    
    else:
        i+=1




print(a)
sum = 0
for i in a:
    sum += int(i[0]) * int(i[1])




print(sum)