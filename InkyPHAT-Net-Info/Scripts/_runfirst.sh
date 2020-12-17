#!/bin/bash
##While creating the scripts for the Pi 0 W, I failed to test for requirements when running on the lite version of raspbianOS.
##The following are the dependencies for the Pi0 W running the lite Raspbian OS.
##Added running the button script as a service so it is always listening for button press.
##Assure git clone https://github.com/madtvmaster90210/inky.git has been run so the folder structure exists.
##MUST HAVE USB DONGLE - SCRIPT DISABLES ONBOARD WIRELESS!!!!



if [ `whoami` != root ]; then
    echo '!!!!Run as sudo!!!!!'
    exit
fi


sudo apt update && sudo apt upgrade -y;
sudo apt install -y python3-pip \
    git \
    libatlas-base-dev \
    python3-numpy \
    libopenjp2-7 \
    libtiff5 \
    python3-buttonshim \
    daemontools \
    daemontools-run \
    lldpd; 
sudo pip3 install inky[rpi,fonts] pillow;
sudo mkdir /etc/service/button;
sudo cp /home/pi/inky/InkyPHAT-Net-Info/Scripts/command.py /etc/service/button/command.py;
echo -e '#!/bin/bash\nexec /usr/bin/python3 command.py' >> /etc/service/button/run;
sudo chmod u+x /etc/service/button/run;
sudo echo -e 'dtoverlay=pi3-disable-wifi\ndtparam=i2c_arm=on\ndtparam=i2s=on\ndtparam=spi_arm=on' >> /boot/config.txt;
sudo reboot
