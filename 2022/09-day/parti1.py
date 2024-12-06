

f = open("inputExemple.txt","r")

f = open("input.txt","r")
data = f.read()

datalist = data.split("\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()

""
priorite = dict()

for i,l in enumerate(alphabet):
    priorite[l] = i+1


score = 0
for sac in datalist:
    s1 = set(sac[:len(sac)//2])
    s2 = set(sac[len(sac)//2:])

    e = s1.intersection(s2)

    score += priorite[e.pop()]

print(score)