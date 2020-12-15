##Script to show IP, Connected Switch Port, Switch Hostname, VLAN Port, date, time


#import boilerplate
import os
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

os.path.dirname(os.path.abspath("/home/pi/inky/Scripts/"))

## Grab IPv4 and define variable additional networking variables
ipv4 = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
switchname = os.popen('lldpctl eth0 | grep -oP "(?<=SysName: ).*" | tr -s [:space:] ').read().strip()
port = os.popen('lldpctl eth0 | grep -oP "(?<=PortID:).*" | tr -s [:space:] |  awk "{print $3}" ').read().strip()
vlan = os.popen('lldpctl eth0 | grep -oP "(?<=VLAN: ).*" | tr -s [:space:] ').read().strip()
datetime = time.strftime("%d/%m %H:%M")

## Load graphic

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

## import text

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 16)
smallfont = ImageFont.truetype(FredokaOne, 14)
bigfont = ImageFont.truetype(FredokaOne, 20)

##Print text
# Top Left
draw.text((6, 7), datetime, inky_display.BLACK, font=font)

# Left
draw.text((6, 30), str("PORT:  ")+str(port), inky_display.BLACK, font=smallfont)
draw.text((6, 50), str("Hostname: "), inky_display.BLACK, font=font)
draw.text((6, 65), str(switchname), inky_display.BLACK, font=font)

# Bottom Row
draw.text((6, 100), str("IP:  ")+str(ipv4), inky_display.YELLOW, font=font)
draw.text((120, 100), str("VLAN:  ")+str(vlan), inky_display.YELLOW, font=font)

# Right

#Top Right


##Flip Screen
#flipped = set_rotation(180)
#inky_display.set_image(flipped)

inky_display.set_image(img)
inky_display.show()
