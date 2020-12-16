#!/bin/bash
##While creating the scripts for the Pi 0 W, I failed to test for requirements when running on the lite version of raspbianOS.
##The following are the dependencies for the Pi0 W running the lite Raspbian OS.
##Added running the button script as a service so it is always listening for button press.
##Assure git clone https://github.com/madtvmaster90210/inky.git has been run so the folder structure exists.
##MUST HAVE USB DONGLE - SCRIPT DISABLES ONBOARD WIRELESS!!!!



sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip git libatlas-base-dev python3-numpy libopenjp2-7 libtiff5 && pip3 install inky[rpi,fonts] && pip3 install pillow && sudo apt-get install python3-buttonshim && sudo apt-get install daemontools daemontools-run && sudo apt install lldpd && sudo mkdir /etc/service/button && sudo cp /home/pi/inky/InkyPHAT-Net-Info/Scripts/command.py /etc/service/button/command.py && echo '#!/bin/bash' >> /etc/service/button/run && echo 'exec /usr/bin/python3 command.py' >> /etc/service/button/run && sudo chmod u+x /etc/service/button/run && sudo chmod u+x /home/pi/inky/InkyPHAT-Net-Info/Scripts/ethnet.py && sudo chmod u+x /home/pi/inky/InkyPHAT-Net-Info/Scripts/wlannet.py && sudo echo 'dtoverlay=pi3-disable-wifi' >> /boot/config.txt && sudo reboot
