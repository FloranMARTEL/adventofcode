

f = open("inputExemple.txt","r")
f = open("input.txt","r")
data = f.read()


lielfe = data.split("\n\n")

m = 0
m2 = 0
m3 = 0
for elfe in lielfe:

    ca = elfe.split("\n")
    
    cptcal = sum([int(c) for c in ca])

    if cptcal >= m:
        m3 = m2
        m2 =  m
        m = cptcal

    elif cptcal >= m2:
        m3 = m2
        m2 =  cptcal
    elif cptcal >= m3:
        m3 = cptcal

print(m)
print(m2)
print(m3)

print(sum([m,m2,m3]))