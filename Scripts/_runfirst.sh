##While creating the scripts for the Pi 0 W, I failed to test for requirements when running on the lite version of raspbianOS.
##The following are the dependencies for the Pi0 W running the lite Raspbian OS


sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip git libatlas-base-dev python3-numpy libopenjp2-7 libtiff5 && pip3 install inky[rpi,fonts] && pip3 install pillow && crontab -l | { cat; echo "@reboot python3 /home/pi/inky/Scripts/command.py.test &"; } | crontab -


