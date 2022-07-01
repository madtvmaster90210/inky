#!/usr/bin/env python3
#This script is to be scheduled with Cron to run at boot in background
#REQUIRES modules below, script should install them
#You must have the fonts and images folder in same directory as script.
#inkycalendar.py and image_processor.py must also be in the same directory.
#Please install python3-pip and python3-numpy prior to running

import os
import apt
import subprocess
import sys
from subprocess import check_call, CalledProcessError
cache = apt.Cache()

def chwd():
    script = os.path.realpath(__file__)
    path = os.path.dirname(script)
    os.chdir(path)

if __name__ == '__main__':
    chwd()

if cache['python3-pip'].is_installed:
	print ("python3-pip is installed")
else: 
	print ("Please run sudo apt install python3-pip.")
	exit()

if cache['python3-numpy'].is_installed:
	print ("python3-numpy is installed")
else:
	print ("Please run sudo apt install python3-numpy.")
	exit()
if cache['libatlas-base-dev'].is_installed: ###only needed for Raspberry Pi's####
	print ("libatlas-base-dev is installed")
else:
	print ("Please run sudo apt install libatlas-base-dev")
	exit()
try:
	from PIL import Image, ImageDraw, ImageFont
except ImportError:
	print("Please run sudo apt install python3-pil")
	exit()
try:
	import RPi.GPIO
except ImportError:
	print("Attempting to install RPi.GPIO")
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'RPi.GPIO'])
try:  
	from inky.inky_uc8159 import Inky
except ImportError:
	print("Attempting to install Inky")
	subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'inky==1.3.1'])

try:
        from font_source_serif_pro import SourceSerifProSemibold
except ImportError:
        print("Attempting to install font 1 of 2")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'font_source_serif_pro'])

try:
        from font_source_sans_pro import SourceSansProSemibold
except ImportError:
        print("Attempting to install font 2 of 2")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'font_source_sans_pro'])


import glob
import argparse
import socket
import sys
import time
import image_processor
import random
from random import randrange
import subprocess
import signal
import RPi.GPIO as GPIO
import textwrap
from PIL import Image, ImageDraw, ImageFont
from inky.inky_uc8159 import Inky, CLEAN, DESATURATED_PALETTE
from inky import Inky7Colour as Inky
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

# minimum time in seconds before the image changes
MIN_SLEEP_BETWEEN_IMAGES = 45

# extensions to load
EXTENSIONS = ('*.png', '*.jpg')

# Gpio pins for each button (from top to bottom)
BUTTONS = [5, 6, 16, 24]

# Set up RPi.GPIO with the "BCM" numbering scheme
GPIO.setmode(GPIO.BCM)

# Buttons connect to ground when pressed, so we should set them up
# with a "PULL UP", which weakly pulls the input signal to 3.3V.
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()

inky = Inky()
saturation = 0
clear = Image.new("P", (inky.width, inky.height), 7)
dpi = 80
cwd = os.getcwd()
cwd_im = (os.getcwd() + "/pictures/")


def reflow_quote(quote, width, font):
    color = "black"
    inky = Inky()
    saturation = 0
    clear = Image.new("P", (inky.width, inky.height), 7)
    words = quote
    reflowed = '"'
    line_length = 0

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n  " + word

    reflowed = reflowed.rstrip() + '"'
    return reflowed

class quoteyMcQuote:
	def show_quote():
		inky_display = Inky()
		w = inky.width
		h = inky.height
		img = Image.new("P", (inky.width, inky.height))
		draw = ImageDraw.Draw(img)
		font_size = 24
		author_font = ImageFont.truetype(SourceSerifProSemibold, font_size)
		quote_font = ImageFont.truetype(SourceSansProSemibold, font_size)
		people = ["Ted"]
		padding = 50
		max_width = w - padding
		max_height = h - padding - author_font.getsize("ABCD ")[1]
		below_max_length = False
		while not below_max_length:
			person = random.choice(people)
			quote = f"Inky Impression is on. Current IP is {ipaddr}. If the images folder has images, they will display shortly." 
			reflowed = reflow_quote(quote, max_width, quote_font)
			p_w, p_h = quote_font.getsize(reflowed)
			p_h = p_h * (reflowed.count("\n") + 1)
			if p_h < max_height:
				below_max_length = True
			else:
				continue
		quote = f"Inky Impression is on. Current IP is {ipaddr}. If the images folder has images, they will display shortly."
		reflowed = reflow_quote(quote, max_width, quote_font)
		p_w, p_h = quote_font.getsize(reflowed)
		p_h = p_h * (reflowed.count("/n") + 2)
		# x- and y-coordinates for the top left of the quote
		quote_x = (w - max_width) / 2
		quote_y = ((h - max_height) + (max_height - p_h - author_font.getsize("ABCD ")[1])) / 2
		# x- and y-coordinates for the top left of the author
		author_x = quote_x
		author_y = quote_y + p_h
		author = "- " + person
		# Draw red rectangles top and bottom to frame quote
		draw.rectangle((padding / 4, padding / 4, w - (padding / 4), quote_y - (padding / 4)), fill=inky_display.RED)
		draw.rectangle((padding / 4, author_y + author_font.getsize("ABCD ")[1] + (padding / 4) + 5, w - (padding / 4), h - (padding / 4)), fill=inky_display.RED)
		# Write our quote and author to the canvas
		draw.multiline_text((quote_x, quote_y), reflowed, fill=inky_display.WHITE, font=quote_font, align="left")
		#draw.multiline_text((author_x, author_y), author, fill=inky_display.WHITE, font=author_font$
		print(reflowed + "\n")
		# Display the completed canvas on Inky wHAT
		inky.set_image(clear)
		inky.set_image(img, saturation)
		inky.show()
		

class ImageFrame:
    images = []
    current_image_index = 0
    path_to_images = cwd_im
    imPro = None

    # Not a lock since this is single threaded and we want to bypass, not wait
    ignore_image_change = False
    clear = Image.new("P", (inky.width, inky.height), 7)

    def __init__(self, path_to_images):
        self.imPro =  image_processor.ImageProcessor()
        self.path_to_images = path_to_images
        self.init_files() 
        self.add_buttons()
  
    def init_files(self):
        for extension in EXTENSIONS:
            self.images.extend(glob.glob("%s/**/%s" % (self.path_to_images, extension), recursive=True))
    
        if len(self.images) == 0:
            error_message = "Error: folder \"%s\" contains no images" % self.images
            self.display_error_message(error_message)
            exit(1)
    def clear_screen(self):
        for _ in range(2):
            for y in range(inky.height - 1):
                for x in range(inky.width - 1):
                    inky.set_pixel(x, y, CLEAN)
            inky.show()
            time.sleep(1.0)

    def display_next_image(self):
        next_image_index = self.current_image_index + 1

        if next_image_index >= len(self.images):
            next_image_index = 0

        self.display_image_by_index(next_image_index)

    def display_previous_image(self):
        prev_image_index = self.current_image_index - 1

        if prev_image_index < 0:
            prev_image_index = len(self.images) - 1

        self.display_image_by_index(prev_image_index)

    def display_error_message(self, error_text, text_color=(0, 0, 0), text_start_height=40):
        image_message = Image.new("RGB", inky.resolution, color=(200, 0, 0))
        font = ImageFont.load_default()
        self.draw_multiple_line_text(image_message, error_text, font, text_color, text_start_height)
        try:
            inky.set_image(image_message, 1)
            inky.show()
        except BaseException as err:
            error_text = "Unexpected {err=}" + {type(err)}
            print(error_text)

    def display_image_by_index(self, number):
        if self.ignore_image_change:
            print('Already changing image... request ignored')
            return
        try:
            self.ignore_image_change = True
            print('Opening and resizing image ', self.images[number])
#            for _ in range(2):
#                for y in range(inky.height - 1):
#                    for x in range(inky.width - 1):
#                        inky.set_pixel(x, y, CLEAN)
#                inky.show()
            image = Image.open(self.images[number])
            resizedimage = image.resize(inky.resolution)
            print('Diffusing image ', self.images[number])
#            self.imPro.diffuse_image(resizedimage)
            print('Displaying image ', self.images[number])
            inky.set_image(resizedimage, 1)
            inky.set_border(inky.BLACK)
            inky.show()
            ignore_image_change = False
        except BaseException as err:
            error_text = "Unexpected error"
            self.display_error_message(error_text)
        finally:
            self.current_image_index = number
            self.ignore_image_change = False

    def display_random_image(self):
        image_index_to_show = randrange(len(self.images))
        self.display_image_by_index(image_index_to_show)

    def draw_multiple_line_text(self, image, text, font, text_color, text_start_height):
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        y_text = text_start_height
        lines = textwrap.wrap(text, width=40)
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text(((image_width - line_width) / 2, y_text),
                    line, font=font, fill=text_color)
            y_text += line_height
     
    def add_buttons(self):
        print('Adding button hooks')
        for pin in BUTTONS:
            GPIO.add_event_detect(pin, GPIO.FALLING, self.handle_button, bouncetime=5000)

    def handle_button(self, pin):
        last_button = BUTTONS.index(pin)
        if last_button == 0:
            imageFrame.clear_screen()
            imageFrame.display_random_image()
        elif last_button == 1:
            imageFrame.clear_screen()
            imageFrame.display_next_image()
        elif last_button == 2:
            imageFrame.clear_screen()
            imageFrame.display_previous_image()
        elif last_button == 3:
            imageFrame.clear_screen()
            subprocess.call(cwd + "/inkycalendar.py", shell=True)
			
imageFrame = ImageFrame(cwd_im)

# start with a image of IP address message!
quoteyMcQuote.show_quote();
while True:
    time.sleep(MIN_SLEEP_BETWEEN_IMAGES)
    imageFrame.clear_screen()
    imageFrame.display_random_image()
