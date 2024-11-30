

f = open("inputExemple.txt","r")
f = open("input.txt","r")
data = f.read()


lielfe = data.split("\n\n")

m = 0

for elfe in lielfe:

    ca = elfe.split("\n")
    
    cptcal = sum([int(c) for c in ca])

    if cptcal >= m:
        m = cptcal


print(m)