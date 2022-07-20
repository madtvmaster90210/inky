##While creating the scripts for the Pi 0 W, I failed to test for requirements when running on the lite version of raspbianOS.
##The following are the dependencies for the Pi0 W running the lite Raspbian OS


sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip git libatlas-base-dev python3-numpy libopenjp2-7 libtiff5 python3-pil && pip3 install inky==1.3.1 && pip3 install rpi.gpio && pip3 install python-resize-image && pip3 install font_source_serif_pro && pip3 install font_source_sans_pro && pip3 install pyowm && pip3 install speedtest-cli


