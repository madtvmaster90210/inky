#!/bin/bash
. /boot/wifi.txt
sudo nmcli d wifi connect $ssid password $password';
sudo rm /boot/wifi.txt
