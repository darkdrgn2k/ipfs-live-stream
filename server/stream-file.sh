#!/bin/sh

#Cleanup old stuff
rm -rf log
rm -rf *.ts
rm -rf *.m3u8


ffmpeg -i $1 -codec:v libx264 -codec:a aac -strict experimental -hls_time 30 -hls_list_size 0 -f hls LIVE.m3u8


