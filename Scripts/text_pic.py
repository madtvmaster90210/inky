##displays text over a picture defined with the "img = " function


#import boilerplate
import os
import socket
from inky.auto import auto
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 32)

inky_display = auto()
colour = inky_display.colour
scale_size = 1
padding = 0
inky_display.set_border(inky_display.WHITE)


# Set current directory

os.chdir(os.path.dirname(os.path.abspath("/home/pi/inky/inky/")))

# Grab IPv4 and define variable

ipv4 = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()

# Load graphic

img = Image.open("/home/pi/inky/inky/PICTURE.png")
draw = ImageDraw.Draw(img)

# Print text
# 
draw.text((40,20), str(ipv4), inky_display.BLACK, font)
#draw.text((20,50), str("%.1f" % round(ratioblocked,2)) + "%", inky_display.BLACK, font)

inky_display.set_image(img)

inky_display.show()
