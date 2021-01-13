#!/usr/bin/env python3
import os
import signal
import buttonshim
import subprocess
import runpy


#wlan = subprocess.call("/home/pi/inky/InkyPHAT-Net-Info/Scripts/wlannet.py", shell=True)
#eth = subprocess.run("/home/pi/inky/Scripts/ethnet.py").read().strip()

@buttonshim.on_press(buttonshim.BUTTON_A)
def handler(button, pressed):
	runpy.run_path(path_name='/home/pi/inky/InkyPHAT-Net-Info/red/Scripts/wlannet.py')

@buttonshim.on_press(buttonshim.BUTTON_B)
def handler(button, pressed):
	runpy.run_path(path_name='/home/pi/inky/InkyPHAT-Net-Info/red/Scripts/ethnet.py')

signal.pause()
