# SongAndDance

The Python scripts cannot run without first installing a Bluetooth package on the Pi. You can do that by executed the following command in the terminal “sudo apt-get install python-bluez”

set up Raspberry Pi to start Python script on startup

sudo crontab -e
@reboot sh /home/pi/launcher.sh >/home/pi/logs/cron.log 2>&1
chmod 755 launch_sd.sh
sh launch_sd.sh

