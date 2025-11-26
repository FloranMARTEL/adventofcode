#parti1
from PIL import ImageDraw,Image,ImageFont
import os

from Gif import *


G = GifMaker(r'Source_Code_Pro\SourceCodePro-VariableFont_wght.ttf',48,(600,1000))


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

##

paddinTop = 50

G.crate_image()
G.writeText((10,10),"L1",fontsize=30)
strl1 = list(map(str,l1))
G.writeText((10,paddinTop),"\n".join(strl1))

G.writeText((10,10),"L2",False,fontsize=30)
strl2 = list(map(str,l2))
G.writeText((30*4,paddinTop),"\n".join(strl2),False)
G.checkImage(1000)


l1.sort()
l2.sort()

G.crate_image()

G.writeText((10,10),"L1",fontsize=30)
strl1 = list(map(str,l1))
G.writeText((10,paddinTop),"\n".join(strl1))

G.writeText((10,10),"L2",False,fontsize=30)
strl2 = list(map(str,l2))
G.writeText((30*4,paddinTop),"\n".join(strl2),False)
G.checkImage(1000)


histdiff = [] 
diff = 0

G.writeText(((G.size[0]//2),10),"diff",False,fontsize=30)
from tqdm import tqdm
for i in tqdm(range(len(l1))):
    diff += abs(l1[i]-l2[i])

    histdiff.append(abs(l1[i]-l2[i]))

    if i < 10:
        strhistdiff = list(map(str,histdiff))
        G.writeText(((G.size[0]//2)-15,paddinTop),"\n".join(strhistdiff),True)
        G.checkImage(100)

    elif i%15  == 0 or i == len(l1)-1:
        G.crate_image()

        G.writeText((10,10),"L1",fontsize=30)
        strl1 = list(map(str,l1[i:]))
        G.writeText((10,paddinTop),"\n".join(strl1))

        G.writeText((10,10),"L2",False,fontsize=30)
        strl2 = list(map(str,l2[i-5:]))
        G.writeText((30*4,paddinTop),"\n".join(strl2),False)

        G.writeText(((G.size[0]//2),10),"diff",False,fontsize=30)
        strhistdiff = list(map(str,histdiff[i-5:]))
        G.writeText(((G.size[0]//2)-30,paddinTop),"\n".join(strhistdiff),True)
        G.checkImage()
    
    


    

G.writeText((10,G.size[1]-60),f'sum(diff) = {diff}',color=(0,255,0))

G.checkImage(2000)

G.creatGIF("gifday1p1")

# import glob
# import contextlib
# # from PIL import Image

# with contextlib.ExitStack() as stack:

#     # lazily load images
#     imgs = (stack.enter_context(Image.open(f))
#             for f in sorted(glob.glob("imgGif/im*")))

#     # extract  first image from iterator
#     img = next(imgs)

#     # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
#     img.save(fp="test.gif", format='GIF', append_images=imgs,
#              save_all=True, duration=200, loop=0)