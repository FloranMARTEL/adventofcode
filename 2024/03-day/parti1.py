#parti1
import re


file = open("inputExemple1.txt","r")
#file = open("input.txt","r")
data = file.read()

#datalist = data.split("\n")
# sum = 0
# d = 0
# while d < len(data)-3:
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

#             if (not faux) and not (len(digit2) == 0 or len(digit1) > 3):
#                 print(digit1,digit2)
#                 sum += int(digit1)*int(digit2)

    

#     d+=1




print("--")
a = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',data)
sum = 0
for i in a:
    sum += int(i[0]) * int(i[1])




print(sum)