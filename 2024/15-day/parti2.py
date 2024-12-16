#parti2


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")

dg = datalist[0].split("\n")
mo = datalist[1]

grid = []

gard = (None,None)

for i in range(len(dg)):
    grid.append([])
    for j in range(len(dg[i])):

        if dg[i][j] == "O":
            grid[i].append("[")
            grid[i].append("]")

        elif dg[i][j] == "@":
            gard = (i,(j*2))

            grid[i].append("@")
            grid[i].append(".")
        else:
            grid[i].append(dg[i][j])
            grid[i].append(dg[i][j])

dirleft = [-1,1]

def left(i,j,t):

    if t:
        d = dirleft[0]
    else:
        d = dirleft[1]
    

    if grid[i][j+(2*d)] == "#":
        return False
    elif grid[i][j+(2*d)] == ".":
        grid[i][j+(2*d)] = grid[i][j+d]
        grid[i][j+d] = grid[i][j]
        return True

    elif grid[i][j+(2*d)] == "]" or grid[i][j+(2*d)] == "[":
        res = left(i,j+(2*d),t)

        if res:
            grid[i][j+(2*d)] = grid[i][j+d]
            grid[i][j+d] = grid[i][j]
        
        return res

    print("bizar")
    return False

dirup = [-1,1]
def up(i,j,t):

    if t :
        d = dirup[0]
    else:
        d = dirup[1]


    if grid[i+d][j] == "#" or grid[i+d][j-1] == "#":
        return False

    elif grid[i+d][j] == "." and grid[i+d][j-1] == ".":
        return True

    elif grid[i+d][j] == "]" and grid[i+d][j-1] == "[":
        re = up(i+d,j,t)
        return re

    elif grid[i+d][j] == "." and grid[i+d][j-1] == "]":
        l = up(i+d,j-1,t)
        return l
    
    elif grid[i+d][j] == "[" and grid[i+d][j-1] == ".":
        r = up(i+d,j+1,t)
        return r

    elif grid[i+d][j] == "[" and grid[i+d][j-1] == "]":
        r = up(i+d,j+1,t)
        l = up(i+d,j-1,t)

        if r and l:
            return True
        else:
            return False
    
    print("bizar")
    return False

def moveup(i,j,t):

    ok = up(i,j,t)
    if ok :

        def rec(i,j,t):
             
            if t :
                d = dirup[0]
            else:
                d = dirup[1]


            if grid[i+d][j] == "#" or grid[i+d][j-1] == "#":
                return False

            elif grid[i+d][j] == "." and grid[i+d][j-1] == ".":
                grid[i+d][j] = "]"
                grid[i+d][j-1] = "["
                grid[i][j] = "."
                grid[i][j-1] = "."

            elif grid[i+d][j] == "]" and grid[i+d][j-1] == "[":
                rec(i+d,j,t)

                grid[i+d][j] = "]"
                grid[i+d][j-1] = "["
                grid[i][j] = "."
                grid[i][j-1] = "."

            elif grid[i+d][j] == "." and grid[i+d][j-1] == "]":
                rec(i+d,j-1,t)

                grid[i+d][j] = "]"
                grid[i+d][j-1] = "["
                grid[i][j] = "."
                grid[i][j-1] = "."
                
            
            elif grid[i+d][j] == "[" and grid[i+d][j-1] == ".":
                rec(i+d,j+1,t)

                grid[i+d][j] = "]"
                grid[i+d][j-1] = "["
                grid[i][j] = "."
                grid[i][j-1] = "."
                

            elif grid[i+d][j] == "[" and grid[i+d][j-1] == "]":
                rec(i+d,j+1,t)
                rec(i+d,j-1,t)

                grid[i+d][j] = "]"
                grid[i+d][j-1] = "["
                grid[i][j] = "."
                grid[i][j-1] = "."
        
        rec(i,j,t)
    
    return ok



n = 0
for m in mo:
    print(n)
    n+=1
    if n == 38:
        print("ici")

    if m == "<":

        r= grid[gard[0]][gard[1]-1] != "#"

        if grid[gard[0]][gard[1]-1] == "]":
            r = left(gard[0],gard[1]-1,True)

        if r:
            grid[gard[0]][gard[1]] = "."
            grid[gard[0]][gard[1]-1] = "@"
            gard = (gard[0],gard[1]-1)

    
    elif m == "^":

        k = grid[gard[0]-1][gard[1]] != "#"

        if grid[gard[0]-1][gard[1]] == "]" or grid[gard[0]-1][gard[1]] == "[":
            

            if grid[gard[0]-1][gard[1]] == "]":
                k = moveup(gard[0]-1,gard[1],True)

                if k:
                    grid[gard[0]-1][gard[1]-1] = "."

            elif grid[gard[0]-1][gard[1]] == "[":
                k = moveup(gard[0]-1,gard[1]+1,True)
                if k:
                    grid[gard[0]-1][gard[1]+1] = "."

        if k:
            grid[gard[0]][gard[1]] = "."
            grid[gard[0]-1][gard[1]] = "@"
            gard = (gard[0]-1,gard[1])

    
    elif m == ">":
        r = grid[gard[0]][gard[1]+1] != "#"

        if grid[gard[0]][gard[1]+1] == "[":
            r = left(gard[0],gard[1]+1,False)

        if r:
            grid[gard[0]][gard[1]] = "."
            grid[gard[0]][gard[1]+1] = "@"
            gard = (gard[0],gard[1]+1)
    

    elif m == "v":
        
        k = grid[gard[0]+1][gard[1]] != "#"

        if grid[gard[0]+1][gard[1]] == "]" or grid[gard[0]+1][gard[1]] == "[":
            

            if grid[gard[0]+1][gard[1]] == "]":
                k = moveup(gard[0]+1,gard[1],False)

                if k:
                    grid[gard[0]+1][gard[1]-1] = "."

            elif grid[gard[0]+1][gard[1]] == "[":
                k = moveup(gard[0]+1,gard[1]+1,False)
                if k:
                    grid[gard[0]+1][gard[1]+1] = "."

        if k:
            grid[gard[0]][gard[1]] = "."
            grid[gard[0]+1][gard[1]] = "@"
            gard = (gard[0]+1,gard[1])
        
su = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):

        if grid[i][j] == "[":
            su += (i*100 + j)

print(su)




