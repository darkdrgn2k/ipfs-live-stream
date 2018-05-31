#!/bin/sh
sudo modprobe bcm2835-v4l2
sudo v4l2-ctl --set-ctrl video_bitrate=100000
ffmpeg  -f alsa -ac 1 -i hw:1 -f video4linux2 -input_format h264 -video_size 1280x720 -framerate 30 -i /dev/video0  -vcodec copy -hls_time 10 LIVE.m3u8



