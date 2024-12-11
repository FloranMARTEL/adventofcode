#parti1

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split(" ")


def plus5(v):
    li = [v]
    a=5
    while a > 0:
        j = 0
        while j < len(li):
            if li[j] in dicp:
                val = dicp[li[j]]
                ll = len(val)
                if ll >= 5:
                    a = reversed(val[4])
                else:
                    a = 
                
                del datalist[j]
                for val in a:
                    li.insert(j,val)



            if li[j] == "0":
                li[j] = "1"
            elif len(li[j])%2 == 0:
                p = li[j]
                p1 = p[:len(p)//2]
                p2 = p[len(p)//2:]
                p2 = str(int(p2))

                del li[j]
                li.insert(j,p2)
                li.insert(j,p1)
                j+=1
            else:
                li[j] = str(int(li[j]) * 2024)
            
            j+=1

        a-=1
    return li


# i = 75
# while i > 0:
#     print(i)
#     j = 0
#     while j < len(datalist):
#         if datalist[j] == "0":
#             datalist[j] = "1"
#         elif len(datalist[j])%2 == 0:
#             p = datalist[j]
#             p1 = p[:len(p)//2]
#             p2 = p[len(p)//2:]
#             p2 = str(int(p2))

#             del datalist[j]
#             datalist.insert(j,p2)
#             datalist.insert(j,p1)
#             j+=1
#         else:
#             datalist[j] = str(int(datalist[j]) * 2024)
        
#         j+=1

#     i-=1
dicp = dict()
dic = dict()
i = 75//5
while i > 0:
    print(i)
    j = 0
    while j < len(datalist):
        v : list
        if datalist[j] in dic:
            v = dic[datalist[j]]
            a = reversed(v)
            del datalist[j]
            for val in a:
                datalist.insert(j,val)
        else:
            v = plus5(datalist[j])
            dic[datalist[j]] = v

            a = reversed(v)
            del datalist[j]
            for val in a:
                datalist.insert(j,val)

        j+=len(v)



    
    

    i-=1


print(len(datalist))