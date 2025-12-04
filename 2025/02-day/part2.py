#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()


datalist = data.split(",")


def iv(i):

    s = str(i)

    i = 2

    while i <= len(s):

        if len(s)%i == 0:

            v = s[:len(s)//i]
            equ = False
            for j in range(1,i):
                id = (len(s)//i)*j
                iff = (len(s)//i)*j + len(s)//i
                vii= s[id:iff]
                if v != vii:
                    equ = True
            
            if equ == False:
                return False

        i+=1
    
    return True
            


    
    # return s[:len(s)//2] != s[len(s)//2:]

su = 0
for l in datalist:

    [v1,v2] = l.split("-")

    v1 = int(v1)
    v2 = int(v2)

    for i in range(v1,v2+1):


        if iv(i) == False:
            su += i


print(su)