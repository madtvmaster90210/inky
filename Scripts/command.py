#!/usr/bin/env python 3
import os
import signal
import buttonshim
import subprocess
import runpy


#wlan = subprocess.call("/home/pi/inky/Scripts/wlannet.py", shell=True)
#eth = subprocess.run("/home/pi/inky/Scripts/ethnet.py").read().strip()

@buttonshim.on_press(buttonshim.BUTTON_A)
def handler(button, pressed):
	runpy.run_path(path_name='/home/pi/inky/Scripts/wlannet.py')

@buttonshim.on_press(buttonshim.BUTTON_B)
def handler(button, pressed):
	runpy.run_path(path_name='/home/pi/inky/Scripts/ethnet.py')

signal.pause()
