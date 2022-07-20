#!/bin/bash
##While creating the scripts for the Pi 0 W, I failed to test for requirements when running on the lite version of raspbianOS.
##The following are the dependencies for the Pi0 W running the lite Raspbian OS
if [ `whoami` != root ]; then
    echo '!!!!Run as sudo!!!!!'
    exit
fi

sudo apt update && sudo apt upgrade -y;
sudo apt install python3-pip \
    git \
    libatlas-base-dev \
    python3-numpy \
    libopenjp2-7 \
    libtiff5 \
    python3-pil;
pip3 install inky==1.3.1 rpi.gpio python-resize-image font_source_serif_pro font_source_sans_pro pyowm speedtest-cli;
sudo echo -e '\ndtparam=i2c_arm=on\ndtparam=spi=on' >> /boot/config.txt;
sudo reboot


