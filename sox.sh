#!/bin/sh

filename=$1
duration=$2

#echo $duration


# USB C-Media
arecord -D hw:1,0 -d $duration -f S16_LE > $filename

# SD-90
#arecord --format S24_3LE -c 2 --rate 44100 -d $duration $filename

# Analyser
sox $filename -n stat 2>&1 | sed -n 's#^Maximum amplitude:[^0-9]*\([0-9.]*\)$#\1#p'
