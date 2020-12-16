##This script is to be run as a cron job upon reboot or cold boot, to show the current IP address of the Pi.

#boilerplate
import os
from inky.auto import auto
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
import time
import subprocess

#set display
inky_display = auto()
colour = inky_display.colour
scale_size = 1
padding = 0
inky_display.set_border(inky_display.WHITE)

#set path
os.path.dirname(os.path.abspath("/home/pi/inky/Scripts/"))

#Set variables
cmd = "ifconfig wlan0 | grep 'inet 10' | cut -c 14-25"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
ipv4 = ps.communicate()[0]

#Set time variable
datetime = time.strftime("%d/%m %H:%M")

#Set image
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

#define font
from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 16)

# Draw from Top Left
draw.text((6, 7), datetime, inky_display.BLACK, font=font)

# Draw on Bottom Row
draw.text((6, 100), str("IP:  ")+str(ipv4), inky_display.YELLOW, font=font)

inky_display.set_image(img)
inky_display.show()
