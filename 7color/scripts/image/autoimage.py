#!/usr/bin/env python3
#Script to convert/resize random image from folder and display on inky
import os
try:
        import PIL, inky.inky_uc8159, schedule
except ImportError:
        print ("Trying to Install require module: pillow, inky, schedule\n")
        os.system('python3 -m pip 3 install pillow, inky')
        os.system('python3 -m pip install schedule')

print ("Modules have been installed successfully, continueing with script.\n")

# import modules needed
import PIL
from inky.inky_uc8159 import Inky, CLEAN
import random
import schedule
import time
from PIL import Image
from resizeimage import resizeimage

# set inky and saturation variable

inky = Inky()
saturation = 0.5
w = inky.width
h = inky.height

# Define the scheduled job
def autoimage():
        print ("Clearing pallette.\n")
        clear = Image.new("P", (inky.width, inky.height), 7)
        inky.set_image(clear)
        inky.show()


## Select random picture from designated folder
        print ("Setting image now!.\n")
        cwd = (os.getcwd() + "/images/")
        d = random.choice(os.listdir(cwd))
        image = Image.open(cwd + d).resize((600,448)).convert('RGB')
        
## Set image to display
        inky.set_image(image, saturation=saturation)
        inky.show()
schedule.every(30).seconds.do(autoimage) ##set schedule
while True:
        schedule.run_pending()
        time.sleep(0)

