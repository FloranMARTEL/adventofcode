
import os, shutil
from PIL import Image, ImageFont, ImageDraw

class GifMaker:

    def __init__(self, fontpath, fontsize,size):
        
        self.fontpath = fontpath
        self.fontsize = fontsize

        self.size = size

        self.image = None
        self.histImage = []
        self.fps = []
    

    # def clear(self):
    #     #dealet all
    #     folder = 'imgGif'
    #     for filename in os.listdir(folder):
    #         file_path = os.path.join(folder, filename)
    #         if os.path.isfile(file_path) or os.path.islink(file_path):
    #             os.unlink(file_path)

    
    def crate_image(self):
        self.image =Image.new("RGBA",(self.size[0],self.size[1]),(0,0,0,0))


    
    def writeText(self,position,text,left = True,fontsize = None,color = None):

        if color == None:
            color = (255,255,255)
        
        if fontsize == None:
            fontsize = self.fontsize

        if left == False:
            position = (self.size[0]-position[0]-30,position[1])
         
        font = ImageFont.truetype(self.fontpath, fontsize) 
        
        drawer = ImageDraw.Draw(self.image)

        drawer.multiline_text(position,text,font=font,fill=color)

    def debugCruentImage(self):

        self.image.show()
        

    def checkImage(self,nb_frame=100):
        self.histImage.append(self.image.copy())
        self.fps.append(nb_frame)

    def creatGIF(self,name):

        if len(self.histImage) == 0:
            return
        
        it = iter(self.histImage)
        v1 = next(it)
        v1.save(fp=name+".gif", format='GIF', append_images=it,
             save_all=True, duration=self.fps,
             loop=0, subrectangles = True)
