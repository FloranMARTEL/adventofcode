#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n\n")


seeds = list(map(int,datalist[0].split(":")[1].split(" ")[1:]))

print(seeds)
m = None
for si in range(len(seeds)//2):
    so = [(seeds[si*2],seeds[(si*2)+1])]


    for l in datalist[1:]:

        inter = l.split("\n")[1:]

        for sii,s in enumerate(so):

            for i in inter:
                i = i.split(" ")
                i = list(map(int,i))

                f = s[0]+s[1]
                d = s[0]
                if d >= i[1] and d < i[1]+i[2]:
                    newd = d
                    newf = f
                    if f > i[1]+i[2]:
                        newf = i[1]+i[2]
                        if f-newf != 0:
                            so.append((newf,f-newf))

                    newd = newd-i[1]+i[0]
                    newf = newf-i[1]+i[0]

                    so[sii] = (newd,newf-newd)
                    
                    break
                elif f > i[1] and f < i[1]+i[2]:
                        newd = i[1]
                        if d-newd != 0:
                            so.append((d,newd-d))

                        newd = newd-i[1]+i[0]
                        newf = f-i[1]+i[0]

                        so[sii] = (newd,newf-newd)


                        break

                # if s >= i[1] and s < i[1]+i[2]:
                #     s = s-i[1]+i[0]
                #     break

    for s in so:   
        if m == None or m > s[0]:
            m = s[0]

print("m : ",m)