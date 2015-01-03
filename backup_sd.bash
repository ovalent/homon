#!/bin/bash

# Script tp create an image file from SD card and compress it
# SD card is suposely in /dev/sdb
# NOTE: run this scrip with sudo!
echo NOTE: run this scrip with sudo!

#SDcard location
VAR_SDcard=/dev/sdb

#output file name
VAR_outputfile=sdimage_`date +%Y%m%d-%H%M%S`.img
VAR_outputzipfile=$VAR_outputfile.gz

#output folder
VAR_outputfolder=/home/oli/raspberry/sd_images/

#get SD card size
VAR_SDsize=$(blockdev --getsize64 $VAR_SDcard)
echo SD card: $VAR_SDcard \(size: $VAR_SDsize\)

echo Creating img file from SD card \($VAR_outputfolder$VAR_outputfile\)...
#dd if=$VAR_SDcard of=$VAR_outputfolder$VAR_outputfile;
pv -tpreb -s $VAR_SDsize $VAR_SDcard | dd of=$VAR_outputfolder$VAR_outputfile;
#dd if=$VAR_SDcard bs=4096 | pv -tpreb -s $VAR_SDsize | dd bs=4096 of=$VAR_outputfolder$VAR_outputfile

echo Compressing $VAR_outputfile to $VAR_outputzipfile...
pv -tpreb $VAR_outputfolder$VAR_outputfile | pigz > $VAR_outputfolder$VAR_outputzipfile

echo Delete $VAR_outputfile file...
rm $VAR_outputfolder$VAR_outputfile

echo Done !