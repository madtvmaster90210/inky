#!/usr/bin/env python3
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

os.path.dirname(os.path.abspath("/home/pi/inky/InkyPHAT-Net-Info/Scripts/"))



## Grab IPv4 and define variable additional networking variables

ipv4 = os.popen('ip addr show wlan0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
#wlan = os.popen('iw wlan0 station dump | grep "signal:" | tr  -d "[:blank:]" ').read().strip()
wlan = os.popen('iwconfig wlan0 | grep -i --color quality | cut -c 45-50').read().strip()
mac = os.popen('iwlist wlan0 scan | grep "Cell 01" | sed -n -e "s/^.*Address://p" ').read().strip()
AccessPoint = os.popen('iwgetid -r').read().strip()

datetime = time.strftime("%d/%m %H:%M")




## Load graphic

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)



## import text

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 14)
smallfont = ImageFont.truetype(FredokaOne, 12)
bigfont = ImageFont.truetype(FredokaOne, 16)



##Print text
# Top Left
draw.text((0, 0), datetime, inky_display.BLACK, font=font)

# Left
draw.text((0, 20), str("BSSID:  ")+str(AccessPoint), inky_display.BLACK, font=smallfont)
draw.text((0, 40), str("MAC:  ")+str(mac), inky_display.BLACK, font=font)

# Bottom Row
draw.text((0, 80), str("IP:  ")+str(ipv4), inky_display.YELLOW, font=font)

# Right

#Top Right
draw.text((85, 0), str("Signal: ")+str(wlan), inky_display.BLACK, font=font)



#Flip Screen
#flipped = set_rotation(180)
#inky_display.set_image(flipped)

inky_display.set_image(img)
inky_display.show()
