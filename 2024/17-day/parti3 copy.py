#parti1

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
    
        

def nextStep(A):
    B = A%8
    B = B ^ 3
    C = A//(2**B)
    B = B ^ 5
    B = B ^ C
    return B%8

def back(A,pos):

    if pos == 0:
        histoA.append(A)

    if nextStep(A) == prog[pos]:
        
        for newA in range(8):
            back(A*8+newA,pos-1)

def find(A, col=0):
    if nextStep(A) != prog[-(col + 1)]:
        return

    if col == len(prog) - 1:
        histoA.append(A)
    else:
        for B in range(8):
            find(A * 8 + B, col + 1)


histoA = []
for a in range(8):

    # back(a,len(prog)-1)
    find(a)

print(histoA)



a = histoA[0]
ouput = []
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
        print(f"a = {a}")

    elif instru == 1:
        t = b ^ vallit
        b= t
    
    elif instru == 2:
        t = (valcomb%8)
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

newo = list(map(str,ouput))
print(",".join(newo))
print(a)
print(b)
print(c)



