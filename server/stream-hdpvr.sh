#!/bin/sh

v4l2-ctl --device=/dev/video1 --set-ctrl=video_bitrate=812500
#Cleanup old stuff
rm -rf log
rm -rf *.ts
rm -rf *.m3u8

ffmpeg            -f mpegts   -i /dev/video1  -f mpegts -vcodec copy   \
 -hls_time 30 -hls_list_size 0 -f hls \
LIVE.m3u8


