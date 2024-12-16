#parti1

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
        grid[i].append(dg[i][j])

        if dg[i][j] == "@":
            gard = (i,j)

mouve = []

for i in range(len(mo)):
    if mo[i] != "\n": 
        mouve.append(mo[i])


for m in mo:


    if m == "<":
        
        for c in range(gard[1],-1,-1):

            if grid[gard[0]][c] == "#":
                break

            elif grid[gard[0]][c] == ".":

                grid[gard[0]][c] = "O"
                grid[gard[0]][gard[1]] = "."
                grid[gard[0]][gard[1]-1] = "@"
                gard = (gard[0],gard[1]-1)

                break
    
    elif m == "^":
        
        for c in range(gard[0],-1,-1):

            if grid[c][gard[1]] == "#":
                break

            elif grid[c][gard[1]] == ".":

                grid[c][gard[1]] = "O"
                grid[gard[0]][gard[1]] = "."
                grid[gard[0]-1][gard[1]] = "@"
                gard = (gard[0]-1,gard[1])

                break
    
    elif m == ">":
        
        for c in range(gard[1],len(grid[0]),1):

            if grid[gard[0]][c] == "#":
                break

            elif grid[gard[0]][c] == ".":

                grid[gard[0]][c] = "O"
                grid[gard[0]][gard[1]] = "."
                grid[gard[0]][gard[1]+1] = "@"
                gard = (gard[0],gard[1]+1)

                break
    

    elif m == "v":
        
        for c in range(gard[0],len(grid),1):

            if grid[c][gard[1]] == "#":
                break

            elif grid[c][gard[1]] == ".":

                grid[c][gard[1]] = "O"
                grid[gard[0]][gard[1]] = "."
                grid[gard[0]+1][gard[1]] = "@"
                gard = (gard[0]+1,gard[1])

                break
        
su = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):

        if grid[i][j] == "O":
            su += (i*100 + j)

print(su)




