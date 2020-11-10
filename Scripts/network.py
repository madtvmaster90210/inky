#import boilerplate
import os
import socket
from inky.auto import auto
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
import time
import psutil

#set display parameters
inky_display = auto()
colour = inky_display.colour
scale_size = 1
padding = 0

#Set border
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

ram = psutil.virtual_memory().percent
print ("Functions loaded")


datetime = time.strftime("%d/%m %H:%M")

print ("Time has loaded")

# Grab IPv4 and define variable

ipv4 = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | a$

# Load graphic

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# import text
from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 22)

# Print text

# Top Left
draw.text((6, 7), datetime, inky_display.BLACK, font=font)

# Left
##example#draw.text((6, 21), ''.join(map(str, get_up_stats())), inky_display.BLACK, font$
##example#draw.text((6, 31), "T"+str(get_temperature())+"C PR:"+str(get_process_count())$

draw.text((6, 41), str("RAM USAGE:")+str(ram), inky_display.BLACK, font=font)

# Bottom Row
draw.text((6, 87), str("IP  ")+str(ipv4), inky_display.YELLOW, font=font)


# Right



#create and draw the image
inky_display.set_image(img)
inky_display.show()
 
