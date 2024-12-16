#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

l = 101#11
h = 103#7

class rob:
    
    def __init__(self,r,l,vr,vl):
        self.r = r
        self.l = l
        self.vr = vr
        self.vl = vl

    def move(self):
        self.r = (self.r + self.vr)%h
        self.l = (self.l + self.vl)%l


lirob :list[rob] = []
for li in datalist:

    o = li.split(" ")
    k = o[0].split("=")[1]
    pos = k.split(",")

    k = o[1].split("=")[1]
    vi = k.split(",")

    lirob.append(rob(int(pos[1]),int(pos[0]),int(vi[1]),int(vi[0])))

from PIL import ImageDraw,Image,ImageFont

dic = dict()
m = 0
while m < 100000 :

    for r in lirob:
        r.move()

    grid = []

    for i in range(h):
        grid.append([])
        for j in range(l):
            grid[i].append(0)
    
    # im =Image.new("RGB",(h,l),(0,0,0))
    
    for r in lirob:
        grid[r.r][r.l] += 1
        # im.putpixel((r.r,r.l),(255,255,255))

    # draw = ImageDraw.Draw(im)
    # draw.multiline_text((10,10),text=str(m))

    # im.save(f"im/i{str(m).zfill(3)}.png")

    for i in range(0,h-30):
        for j in range(l):
            if grid[i][j] != 0:
                v = grid[i][j]
                ok = True
                for a in range(30):
                    if grid[i+a][j] != v:
                        ok = False
                        break
                
                if ok:
                    im = Image.new("RGB",(h,l),(0,0,0))
                    for r in lirob:
                        im.putpixel((r.r,r.l),(255,255,255))
                    
                    draw = ImageDraw.Draw(im)
                    draw.multiline_text((10,10),text=str(m+1))
                    im.save(f"im/sap{str(m).zfill(4)}.png")

                    print("ici")

                




    print(m)
    m+=1





# import glob
# import contextlib
# # from PIL import Image

# with contextlib.ExitStack() as stack:

#     # lazily load images
#     imgs = (stack.enter_context(Image.open(f))
#             for f in sorted(glob.glob("im/i*")))

#     # extract  first image from iterator
#     img = next(imgs)

#     # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
#     img.save(fp="test.gif", format='GIF', append_images=imgs,
#              save_all=True, duration=500, loop=0)