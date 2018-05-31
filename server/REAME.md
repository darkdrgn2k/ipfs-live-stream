apt-get install ffmpeg inotify-tools

Please  process.sh and a stream-????.sh into a folder

Edit stream-???.sh to select the correct /dev/video? if neeed
for pi enable camera -

sudo raspi-config 
# Select Interface Optiosn
# Select Camera
# Enables Yes
# OK
# FINISH
# Dont reboot


edit process.sh to configure the correect scp line (remember to add keys)


To run

Run ipfs daemon
screen -dms ipfs sudo -H -u pi ipfs daemon
or
screen -dms ipfs ipfs daemon

run ffmpeg
screen -dmS ffmpeg  ./stream-???.sh

run process script
screen -dmS ffmpeg  ./process.sh

