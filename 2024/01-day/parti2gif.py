#parti2


file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")
l1 = [None] * len(datalist)
l2 = l1[:]

for i in range(len(datalist)):
    dd = datalist[i].split("   ")
    l1[i] = int(dd[0])
    l2[i] = int(dd[1])

from Gif import *

G = GifMaker(r'Source_Code_Pro\SourceCodePro-VariableFont_wght.ttf',48,(2000,1500))

paddinTop = 50
G.crate_image()
G.writeText((10,10),"L1",fontsize=30)
strl1 = list(map(str,l1))
G.writeText((10,paddinTop),"\n".join(strl1))


G.writeText((20+5*30,10),"Compteur",fontsize=30)

def strdict(di):
    text = "{"
    i = 0
    for key in di:
        text += f"{key} : {di[key]};  "

        if i%10 == 0:
            text += "\n"
        
        i+=1

    return text+"}"

cptd = dict()
G.writeText((20+5*30,paddinTop),strdict(cptd),fontsize=25)

G.checkImage()
from tqdm import tqdm

for i,v in tqdm(enumerate(l2)):

    if v in cptd:
        cptd[v] += 1
    else:
        cptd[v] = 1

    if i%15 == 0:
        G.crate_image()
        G.writeText((10,10),"L2",fontsize=30)
        strl1 = list(map(str,l1[i:]))
        G.writeText((10,paddinTop),"\n".join(strl1))


        G.writeText((20+5*30,10),"Compteur",fontsize=30)
        G.writeText((20+5*30,paddinTop),strdict(cptd),fontsize=15)

        G.checkImage()


imgcopy = G.image.copy()

score = 0
for i,v in enumerate(l1):

    mu = 0
    if v in cptd:
        mu = cptd[v]
        score+= v*mu

    if i%10 == 0 or i == len(l1):
        G.image = imgcopy.copy()
        G.writeText((10,10),"L1",False,fontsize=30)
        strl2 = list(map(str,l2[i:]))
        G.writeText((30*4,paddinTop),"\n".join(strl2),False)

        G.writeText((600,paddinTop),f"{v} x {mu}\nscore={score}",False,color=(255,255,0))

        G.checkImage()
        # G.debugCruentImage()

G.image = imgcopy.copy()
G.writeText((10,10),"L1",False,fontsize=30)
strl2 = list(map(str,l2[i:]))
G.writeText((30*4,paddinTop),"\n".join(strl2),False)
G.writeText((600,paddinTop),f"{v} x {mu}\nscore={score}",False,color=(0,255,0))
G.checkImage(1000)

G.creatGIF("gifday1p2")
    
print(score)
