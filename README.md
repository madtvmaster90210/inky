# inky #
My InkyPHAT Scripts
 =============
The following page includes scripts I created or modified for the Pimoroni InkyPHAT eInk display.
Additional github's I utilized for code:
* https://github.com/pimoroni/button-shim
* https://github.com/KodeMunkie/inky-impression-slideshow
* https://github.com/pimoroni/inky/blob/master/

## InkypHat ##
The InkyPhat scripts here currently only work for the red or yellow display (I cannot recall). This is the 250x122 pixel e-paper display. The Library is Python3.

This script assumes you have a rapsberry Pi connected to the InkypHat red display, as well as the Pimoroni Button Shim connected.

The InkyPHAT-Access-Point-Info will only give wireless Access Point information.

The InkyPHAT-Net-Info will give you both wireless access point information, as well as switch port information if connected to the ethernet port.

***You must have USB Wireless dongle - script will DISABLE onboard wireless adapter, as it is not reliable.***

1. Git clone repo `https://github.com/madtvmaster90210/inky.git`
2. Adjust the wifi.txt file with your known wireless network info.
3. Copy the wifi.txt file into your /boot partition
4. run the _runfirst.sh script
5. If all went well (which is never the case) the display should now show wifi and wired info depending on button selected.
* Button 1 - Display Wireless Info
* Button 2 - Display Wired Info


## Inky Impression ##
Script involves showing random picutres from the 'images' folder obtained with a git clone. Folder structure MUST exist as is in order for the script to call upon the correct assets. This was also done with Python3 library.
1. Git clone repo `https://github.com/madtvmaster90210/inky.git`
2. create Cron job to run main.py script at reboot.
3. Use WinSCP or another method to put images (Must be .JPG or .PNG format) in the images folder.
4. Reboot!

The button layout is as follows:
* Button 1 - Random image
* Button 2 - Next image from folder
* Button 3 - Previous image from folder
* Button 4 - Show Calendar

Upon reboot, the device will display the IP address of it's wireless connection. 


Inky Python3 Library - https://github.com/pimoroni/inky 

Inky Basics - https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat

PiHole with Inky setup - https://github.com/neauoire/inky-hole/blob/master






