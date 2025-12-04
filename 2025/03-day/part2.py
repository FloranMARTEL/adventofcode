#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


def mymax(l,i,j):
    max = None
    index = None
    for i in range(i,j):
        if max == None or max < l[i]:
            max = l[i]
            index = i
    
    return max,index


def cn(l,i,n):

    if n == 0:
        return ""
    
    m,id = mymax(l,i+1,len(l)-(n-1))        

    return str(m)+cn(l,id,n-1)


su = 0
for l in datalist:

    l2 = map(int,l)

    v = cn(l,-1,12)

    su += int(v)
    print(v)


print("su : ",su )
    



