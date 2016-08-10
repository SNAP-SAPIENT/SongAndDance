# SongAndDance


set up Raspberry Pi to start Python script on startup

sudo crontab -e
@reboot sh /home/pi/launcher.sh >/home/pi/logs/cron.log 2>&1
chmod 755 launch_sd.sh
sh launch_sd.sh

