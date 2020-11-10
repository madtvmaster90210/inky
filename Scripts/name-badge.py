import os

#import boilerplate
from inky.auto import auto
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
#in case you need this for later
import argparse

#import fonts
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive


#Set display and scaling and colour

inky_display = auto()
colour = inky_display.colour
scale_size = 1
padding = 0


## inky_display.set_rotation(180)
inky_display.set_border(inky_display.BLACK)

# Create a new canvas to draw on
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# Load the fonts

intuitive_font = ImageFont.truetype(Intuitive, int(22 * scale_size))
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(35 * scale_size))
hanken_medium_font = ImageFont.truetype(HankenGroteskMedium, int(16 * scale_size))

# Grab the name to be displayed

name = "Name"

# Top and bottom y-coordinates for the white strip

y_top = int(inky_display.HEIGHT * (5.0 / 10.0))
y_bottom = y_top + int(inky_display.HEIGHT * (4.0 / 10.0))

# Draw the yellow, white, and yellow strips

for y in range(0, y_top):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.YELLOW)

for y in range(y_top, y_bottom):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.WHITE)

for y in range(y_bottom, inky_display.HEIGHT):
    for x in range(0, inky_display.width):
        img.putpixel((x, y), inky_display.YELLOW)

# Calculate the positioning and draw the "Hello" text

hello_w, hello_h = hanken_bold_font.getsize("Hello")
hello_x = int((inky_display.WIDTH - hello_w) / 2)
hello_y = 0 + padding
draw.text((hello_x, hello_y), "Hello", inky_display.WHITE, font=hanken_bold_font)

# Calculate the positioning and draw the "my name is" text

mynameis_w, mynameis_h = hanken_medium_font.getsize("my name is")
mynameis_x = int((inky_display.WIDTH - mynameis_w) / 2)
mynameis_y = hello_h + padding
draw.text((mynameis_x, mynameis_y), "my name is", inky_display.WHITE, font=hanken_medium_font)

# Calculate the positioning and draw the name text

name_w, name_h = intuitive_font.getsize(name)
name_x = int((inky_display.WIDTH - name_w) / 2)
name_y = int(y_top + ((y_bottom - y_top - name_h) / 2))
draw.text((name_x, name_y), name, inky_display.BLACK, font=intuitive_font)

# Display the completed name badge

inky_display.set_image(img)
inky_display.show()
