#parti2

#a == [8**9;8**10[ = 134_217_728, 1_073_741_823
print((8**10))

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


t = datalist[0].split(":")
a = int(t[1])

t = datalist[1].split(":")
b = int(t[1])

t = datalist[2].split(":")
c = int(t[1])


t = datalist[4].split(":")
prog = t[1][1:].split(",")
prog = list(map(int,prog))

def getcombo(val):

    if val in (0,1,2,3):
        return val
    elif val == 4:
        return a
    elif val == 5:
        return b
    elif val == 6:
        return c
    else :
        None
    
from tqdm import tqdm      

for j in tqdm(range(134_217_728,1_073_741_823+1)):

    ouput = []
    # i = len(prog)-2
    # while i >= 0:
    i = 0
    while i < len(prog):

        instru = prog[i]
        vallit = prog[i+1]
        valcomb = getcombo(vallit)
        out=None
        jump = False

        if instru == 0:
            t = a//(2**(valcomb))
            a = t

        elif instru == 1:
            t = b ^ vallit
            b= t
        
        elif instru == 2:
            t = (valcomb%8)%7
            b = t

        elif instru == 3:
            if a != 0:
                i = vallit
                jump = True
        elif instru == 4:
            t = b ^ c
            b = t
        elif instru == 5:
            out = valcomb % 8

        elif instru == 6:
            t = a//(2**(valcomb))
            b = t
        elif instru == 7:
            t = a//(2**(valcomb))
            c = t




        if out != None: 
            ouput.append(out)
        

        if not jump:
            i+=2

    
    if ouput == [2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]:
        break

newo = list(map(str,ouput))
print(ouput)
print(len(ouput))
print(",".join(newo))
print(a)
print(b)
print(c)



