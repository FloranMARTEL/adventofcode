#parti1

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")


co = []
for l in datalist:

    c = l.split(",")
    c = list(map(int,c))
    co.append(c)

co = list(map(lambda x : (x[0],x[1]), co))
sco = set(co)

co.sort(key=lambda x: x[0])
zon = []

co2 = co[:]

# b = None
# h = None
# d = None
# i=0
# while len(co2) > i:
#     print(i)
#     v = co[i]

#     if b == None:
#         b = v
#     elif h == None:
#         if v[1] > b[1]:
#             h = b
#             b = v
#         else:
#             h = v
#     else:
#         if v[0] == b[0]:
#             if v != v2:
#                 if b == v2:
#                     b= b
#                 else:
#                     h = v
#             # if v[1] > b[1]:
#             #     b = v
#             # elif v[1] < h[1]:
#             #     h = v
#         else:
#             j = i
#             while True:
#                 v2 = co[j]

#                 if v2[1] == h[1] or v2[1] == b[1]:
#                     break

#                 j+=1
            

#             i-=1
#             if v2[1] == h[1]:
#                 zon.append((b,v2))
#                 h = v2
#                 b = (v2[0],b[1])
#             else:
#                 zon.append((h,v2))
#                 b = v2
#                 h = (v2[0],h[1])

#     i+=1

def be(a,b,v):

    if a < b:
        return a < v < b
    else:
        return a > v > b

def be2(a,b,v):

    if a < b:
        return a <= v <= b
    else:
        return a >= v >= b

di = dict()
fi = []
for i in range(len(co)):
    c1 = co[i]
    for j in range(i+1,len(co)):
        c2 = co[j]
        for k in range(j+1,len(co)):
            c3 = co[k]
            
            l = None
            cx= None
            if c1[0] == c2[0]:
                l = (c1,c2)
                cx = c3
            elif c2[0] == c3[0]:
                l = (c2,c3)
                cx = c1
            elif c3[0] == c1[0]:
                l = (c3,c1)
                cx = c2
            
            if l == None:
                continue

            if cx[1] == l[0][1]:
                di[cx] = (cx,l[1])
                fi.append(cx)
            elif cx[1] == l[1][1]:
                di[cx] = (cx,l[0])
                fi.append(cx)


fi.sort(key=lambda x:x[0])
print("ici")
o = co[0]
os = None
s = 0

def seek(a,b,d,f):

    while True:

        o = ((f-d)//2)+d

        vo = fi[o]

        if vo[0] < a[0]:
            d = o
        elif v[0] > b[0]:
            f = o
        else:
            n = fi[o-1]
            m = fi[o+1]

            if be2(a[1],b[1],n):
                v = n
            elif be2(a[1],b[1],o):
                v = o
            elif be2(a[1],b[1],m):
                v = p
            break
    
    # v trouver
     

while s < len(co):
    os = s

    v = co[s]
    
    i = 1
    while True:
        v2 = co[s+i]
        v3 = co[s-i]

        if v2[0] == v[0]:
            


            s = s+i
            break

        if v3[0] == v[0]:
            s = s-i 
            break
        i+=1












def coinzone(c):

    for z in zon:

        if be2(z[0][0],z[1][0],c[0]) and be2(z[0][1],z[1][1],c[1]):
            return False

    return True

ma = None
for i in range(len(co)):
    # print(i)
    for j in range(i+1,len(co)):

        c1 = co[i]
        c2 = co[j]


        if c1 == [9,5] and c2 == [2,3]:
            print("ici")

        er = False
        for o in range(len(co)):
            c3 = co[o]

            if c3 != c1 and c3 != c2:

                if be(c1[0],c2[0],c3[0]) and be(c1[1],c2[1],c3[1]):
                    er = True
                    break
        
        if er == True:
            continue
                
        
        pos = [c1,c2,(c1[0],c2[1]),(c2[0],c1[1])]
        oo = True
        for p in pos:
            if coinzone(p):
                oo = False
                break
        
        if oo == False:
            continue
        
        a = (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)

        if ma == None or a > ma:
            ma = a

print(ma)

