#!/bin/sh

what='LIVE'

while true; do
    x=`ls $what*.ts`

    if ! [ -z "$x" ]; then
        #Wait for file to finish writing
        inotifywait -e close_write $x
        #Add it to IPFS and log the hash
        l=`cat $what.m3u8  | grep -B1 $x | grep "#" | awk -F : '{print $2}' | tr -d ,`
        t=`date '+%Y-%m-%d %H:%M:%S'`
        ipfs add $x >> log
        sed -i  "s#$x#$x $l $t#" log


        #remove the file
        rm $x
        # Re-write teh M3U8 file with the new ipfs hashes from the LOG
        cp $what.m3u8 test.m3u8
        while read p; do
          h=$(echo "$p" | awk '{print $2}') #Hash
          f=$(echo "$p"| awk '{print $3}') #File Name
        sed -i  "s#$f#https://ipfs.io/ipfs/$h#" test.m3u8
        done <log

        sed -i "s/EXTM3U/EXTM3U\n#EXT-X-PLAYLIST-TYPE:EVENT/" test.m3u8
        # Upload to the client

        # M3U8  ipns code (noit working)
#       h=$(ipfs add test.m3u8 | awk '{print $2}')
#       p=$(ipfs name publish $h)
#       echo $p

#SCP Code
        scp test.m3u8 user@node2.e-mesh.net:/var/www/html/tv/stream.m3u8

        # Possible Test - Fore the gateway to grab a copy right away
#       wget https://ipfs.io/ipfs/$h -o /dev/null -T 3 &
    fi
done
