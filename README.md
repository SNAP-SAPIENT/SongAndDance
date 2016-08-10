# SongAndDance


set up Raspberry Pi to start Python script on startup

sudo crontab -e
@reboot sh /home/pi/launch_sd.sh >/home/pi/logs/song_dance 2>&1
chmod 755 launch_sd.sh
sh launch_sd.sh

