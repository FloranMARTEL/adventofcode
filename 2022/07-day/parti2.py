

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")


res = []
resname = []

class Tree:

    def __init__(self,name="/",parent = None) -> None:
        self.parent = parent
        self.name = name
        self.childs : list["Dir"|"File"] = []

    
    def getchildbyname(self,name):
        for c in self.childs:
            if Dir.__instancecheck__(c) and c.name == name:
                return c
        
        return None
    
    def gettail(self):
        global res,resname
        sum = 0
        for c in self.childs:
            sum += c.gettail()
        
        print(f"{self.name} {sum}")

        res.append(sum)
        resname.append(self.name)

        return sum
                
        
    
    def add(self,element : "Dir" or "File"):
        self.childs.append(element)


class Dir(Tree):
    def __init__(self,name,parent) -> None:
        super().__init__(name,parent)




class File:
     
    def __init__(self,tail,name) -> None:
        self.tail = tail
        self.name = name
    
    def gettail(self):
        return self.tail



l = 1

t = Tree()
curentPosition = t


while l < len(datalist):
    ligne = datalist[l]
    if ligne[0] == "$":
        elements = ligne.split(" ")
        com = elements[1]

        if com == "cd":
            arg = elements[2]

            if arg == "/":
                curentPosition = t
            elif arg == "..":
                curentPosition = curentPosition.parent
            else:
                curentPosition = curentPosition.getchildbyname(arg)
        
        elif com == 'ls':

            while l+1 < len(datalist):

                l+=1

                lsligne = datalist[l]
                if lsligne[0] == "$":
                    l -= 1
                    break
                else:
                    elements = lsligne.split(" ")
                    if elements[0] == "dir":
                        curentPosition.add(Dir(elements[1],curentPosition))
                    else:
                        curentPosition.add(File(int(elements[0]),elements[1]))


    

    l+=1

ta = t.gettail()
print("---")

tt = -(70000000 - ta)+30000000
print(tt)
print(len(res))

for i in range(len(res)-1,-1,-1):
     if res[i] < tt:
         del res[i]
         del resname[i]

print(res)
print(resname)
m = min(res)

for i,v in enumerate(res):
    if v == m:
        print("---")
        print(resname[i])

print(3579501+(70000000 - ta) > 30000000)