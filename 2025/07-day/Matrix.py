import numpy as np

class Matrix:

    def __init__(self,li,type = None):
        self.list = []
        for l in range(len(li)):
            self.list.append([])
            for c in range(len(li[l])):

                if type == None:
                    self.list[l].append(li[l][c])
                else:
                    self.list[l].append(type(li[l][c]))

    
    def get(self):
        return Matrix(self.list)

    def getVert(self):
        return Matrix(np.array(self.list).T)
    
    def getdiagDG(self):
        diago = []

        for i in range(len(self.list)+len(self.list[0])):
            diago.append([None]*len(self.list[0]))

        for i in range(len(self.list)):
            for j in range(len(self.list[0])):
                diago[i-j+len(self.list[0])-1][j] = self.list[i][j]
        
        return Matrix(diago)
    

    def getdiagGD(self):
        diago2 = []

        for i in range(len(self.list)+len(self.list[0])):
            diago2.append([None]*len(self.list[0]))

        for i in range(len(self.list)):
            for j in range(len(self.list[0])):
                j2 = abs(len(self.list[0])-1-j)
                diago2[i-j2+len(self.list[0])-1][j] = self.list[i][j]
        
        return Matrix(diago2[:-1])
    
    def convLigneIntoString(self):
        newli = []
        for l in range(len(self.list)):
            text = ""
            for c in range(len(self.list[l])):
                if self.list[l][c] == None:
                    continue

                text += str(self.list[l][c])
            newli.append(text)

        return newli


    
    def __str__(self):
        text = ""
        for l in range(len(self.list)):
            text += "["

            for c in range(len(self.list[l])):
                
                if str(self.list[l][c]) == ".":
                    text+=" "
                    continue
                text+=str(self.list[l][c])

                # if c != len(self.list[l])-1:
                #     text+=""

            text += "]\n"
        
        return text

    def __repr__(self):
        return self.__str__() 



