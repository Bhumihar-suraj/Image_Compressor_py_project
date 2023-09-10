import PIL
from PIL import Image
import os
import re

mywidth=2000
source_dir="C:\\Users\\Suraj\\Desktop\\img"
dest_dir="C:\\Users\\Suraj\\Desktop\\com\\img"

def resize_pic(old_pic,new_pic,mywidth):
    img=Image.open(old_pic)
    wpercent=(mywidth/float(img.size[0]))
    hsize=int((float(img.size[1]*float(wpercent))))

    img=img.resize((mywidth,hsize),Image.BOX)

    img.save(new_pic,"jpeg")

def entire_directory(source_dir,dest_dir,width):
    files=os.listdir(source_dir)
    i=0
    for file in files:
        i+=1

        old_pic=source_dir +"\\"+ file
        new_pic= dest_dir+file

        # print("old_pic=",old_pic)
        # print("new_pic=",new_pic)

        resize_pic(old_pic,new_pic,width)
        print(i,"done") 

entire_directory(source_dir,dest_dir,mywidth)
