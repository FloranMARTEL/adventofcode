#parti1

file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

datalist = list(map(int,datalist))

mod = 16777216
su = 0
for d in datalist:
    for i in range(2000):
        mul1 = d * 64
        d = (d ^ mul1)%mod

        div1 = d // 32
        d = (d ^ div1)%mod

        mult2 = d * 2048
        d = (d^mult2)%mod
    
    su += d
    
print(su)