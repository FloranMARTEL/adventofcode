

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

screen = []
for l in range(6):
    screen.append([])
    for c in range(40):
        screen[l].append("c")

i = 1
X = 1


for gdataligne in datalist:
    ligne = gdataligne.split(" ")

    instu = ligne[0]

    if instu == "noop":
        pass
    elif instu == "addx":
        vv = None
        if i%40 >=X-1 and i%40 <= X+1:
            vv = "#"
        else:
            vv = "."
        screen[i//40][i%40] = vv
        i+=1
        val = int(ligne[1])
        X += val

    vv = None
    if i%40 >=X-1 and i%40 <= X+1:
        vv = "#"
    else:
        vv = "."
    print("-----")
    showscreen(screen)
    screen[i//40][i%40] = vv
    i += 1


showscreen(screen)


