#parti1
from PIL import ImageDraw,Image,ImageFont
import os

import os, shutil
folder = 'imgGif'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)


file = open("inputExemple.txt","r")
# file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")
l1 = [None] * len(datalist)
l2 = l1[:]

for i in range(len(datalist)):
    dd = datalist[i].split("   ")
    l1[i] = int(dd[0])
    l2[i] = int(dd[1])

size = (100+(len(str(max(l1)))*5*2),1000)
space = 15
lenfont = 5
padding = 10

##

im =Image.new("RGB",(size[0]+100,size[1]),(0,0,0))

draw = ImageDraw.Draw(im)

for i in range(len(l1)):
    draw.multiline_text((padding,padding+space*i),str(l1[i]))
    draw.multiline_text((size[0]-len(str(max(l1)))*lenfont-15,padding+space*i),str(l2[i]))

im.save("imgGif/im0001.png")

l1.sort()
l2.sort()

im =Image.new("RGB",size,(0,0,0))

draw = ImageDraw.Draw(im)

for i in range(len(l1)):
    draw.multiline_text((padding,padding+space*i),str(l1[i]))
    draw.multiline_text((size[0]-len(str(max(l1)))*lenfont-15,padding+space*i),str(l2[i]))

im.save("imgGif/im0002.png")



diff = 0

for i in range(len(l1)):
    diff += abs(l1[i]-l2[i])

    p = 10+((size[0]-len(str(max(l1)))*5-15)-10)/2

    draw.multiline_text((p,10+15*i),str(diff))

    im.save(f"imgGif/im{(str(i+3)).zfill(4)}.png")

    if i > 100:
        break

    


print(diff)

import glob
import contextlib
# from PIL import Image

with contextlib.ExitStack() as stack:

    # lazily load images
    imgs = (stack.enter_context(Image.open(f))
            for f in sorted(glob.glob("imgGif/im*")))

    # extract  first image from iterator
    img = next(imgs)

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img.save(fp="test.gif", format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)