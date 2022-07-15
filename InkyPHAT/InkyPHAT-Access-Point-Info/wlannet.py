##Script to show IP, Connected AP, wifi strength, date, time


#import boilerplate
import os
import socket
from inky.auto import auto
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
import time


#Set display for auto detection and configure display variables
inky_display = auto()
colour = inky_display.colour
scale_size = 1
padding = 0
inky_display.set_border(inky_display.WHITE)


#Functions

def shorten(text, length):
    # Process text to be shorter than [length] chars
    str(text)
    if len(text) > length:
        newtext = ""
        for word in text.split():
            newtext += word[0:4]
            newtext += "."
        return(newtext)
    else:
        return(text)


print ("Functions loaded")



## Grab IPv4 and define variable additional networking variables

ipv4 = os.popen('ip addr show wlan0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
wlan = os.popen('iw wlan0 station dump | grep "signal:" | tr  -d "[:blank:]" ').read().strip()
AccessPoint = os.popen('iwgetid -r').read().strip()
datetime = time.strftime("%d/%m %H:%M")

print ("IP Variables Loaded")

## Load graphic

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

print ("Graphics loaded")

## import text

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 16)

print ("Text imported")       
       
##Print text
# Top Left
draw.text((6, 7), datetime, inky_display.BLACK, font=font)

       
# Left
draw.text((6, 41), str("Network:")+str(AccessPoint), inky_display.BLACK, font=font)

# Bottom Row
draw.text((6, 87), str("IP  ")+str(ipv4), inky_display.YELLOW, font=font)

# Right

#Top Right
draw.text((100, 7), wlan, inky_display.BLACK, font=font)

print ("Printing Picture, Look already!")

#Flip Screen
#flipped = set_rotation(180)
#inky_display.set_image(flipped)

inky_display.set_image(img)
inky_display.show()

print ("Done!")
