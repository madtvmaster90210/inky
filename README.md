# inky #
My InkyPHAT and Inky Impression Scripts
 =============
The following page includes scripts I created or modified for the Pimoroni InkyPHAT eInk display.
Additional github's I utilized for code:
* https://github.com/pimoroni/button-shim
* https://github.com/KodeMunkie/inky-impression-slideshow
* https://github.com/pimoroni/inky/
* https://github.com/Hothomir/weather-report

## InkyPHAT ##
The InkyPHAT scripts here currently only work for the red or yellow display (I cannot recall). This is the 250x122 pixel e-paper display. The Library is Python3.

This script assumes you have a rapsberry Pi connected to the InkypHat red display, as well as the Pimoroni Button Shim connected.

The InkyPHAT-Access-Point-Info will only give wireless Access Point information.

The InkyPHAT-Net-Info will give you both wireless access point information, as well as switch port information if connected to the ethernet port.

## Hardware ##

* [Inky Impression](https://shop.pimoroni.com/products/inky-impression-5-7)
* [InkyPHAT](https://shop.pimoroni.com/products/inky-phat)
* [Button Shim for PHAT](https://shop.pimoroni.com/products/button-shim)
* Raspberry Pi
* Wireless USB Dongle
* SD Card

***You must have USB Wireless dongle - script will DISABLE onboard wireless adapter, as it is not reliable.***

***Be sure to enable reqiured GPIO pins (i.e. raspi-config, enable SPI, etc.)***

1. Git clone repo `https://github.com/madtvmaster90210/inky.git`
2. Adjust the wifi.txt file with your known wireless network info.
3. Copy the wifi.txt file into your /boot partition
4. run the _runfirst.sh script
5. If all went well (which is never the case) the display should now show wifi and wired info depending on button selected.
* Button 1 - Display Wireless Info
* Button 2 - Display Wired Info


## Inky Impression ##
***Image quality varies. Future improvements to process may occur, such as messing with dither and saturation.***

Script involves showing random picutres from the 'images' folder obtained with a git clone. Folder structure MUST exist as is in order for the script to call upon the correct assets. This was also done with Python3 library.
1. Git clone repo `https://github.com/madtvmaster90210/inky.git`
2. create Cron job to run main.py script at reboot.
3. Use WinSCP or another method to put images (Must be .JPG or .PNG format) in the images folder.
4. Edit configfile.ini with your API key from OpenWeatherMaps (https://openweathermap.org/api), longitude and latitiude, and 2 digit country code.
5. Reboot!

The button layout is as follows:
* Button 1 - Random image
* Button 2 - Next image from folder
* Button 3 - Show Weather
* Button 4 - Show Calendar

Upon reboot, the device will display the IP address of it's wireless connection. 

# Recurring Display Refreshes
To get new weather information in timed intervals, I've used crontab. Crontab schedules when to run the main.py file and is flexible with how often it should be run. You can also create cron jobs for weather-main.py and inkycalendar.py to have them cycle through periodically, rather than soley rely on the buttons.

I've set up the crontab job to run every 30 minutes, so the display will refresh every 30 minutes. Example:
1. Open crontab in terminal
```
crontab -e
```
2. At the bottom of the crontab file, provide the following line:
```
*/30 * * * * python /home/pi/weather-report/main.py
```
3. To refresh the display every 60 mins (every hour):
```
*/60 * * * * python /home/pi/weather-report/main.py
```


Inky Python3 Library - https://github.com/pimoroni/inky 

Inky Basics - https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat

PiHole with Inky setup - https://github.com/neauoire/inky-hole/blob/master






