#!/bin/bash

# Script to restore a compressed image file to SD card
# SD card is suposely in /dev/sdb
# NOTE: run this scrip with sudo!
echo NOTE: run this scrip with sudo!

# SDcard location
VAR_SDcard=/dev/sdb

# Images files location
VAR_SD_images_folder=/home/oli/raspberry/sd_images/

# Select image file
echo Please select the image you want to restore to SD card:
i=1
for file in $VAR_SD_images_folder*
do
    if [[ -f $file ]]; then
        echo [$i] $file
        image_list[$i]=$file
        ((i++))
    fi
done
((i=i-1))
read -p "Please input your choice (1 to $i)? " answer
if [ "$answer" -lt "1" -o "$answer" -gt "$i" ]; 
    then echo Choice out of range. Exit.;
    exit
fi

VAR_image_z=${image_list[$answer]}
VAR_image_z_size=$(stat -c%s "$VAR_image_z")

VAR_image=`echo $VAR_image_z| cut -d'.' -f -2`
echo 
echo Image selected: $VAR_image

# Confirm copy operation
read -p "Are your sure you want to restore this img to SD card (Y/n)? " answer2
if [ "$answer2" != "Y" ];
    then echo Not sure. Exit.;
    exit
fi
echo
exit
echo [1/3] uncompressing $VAR_image_z to $VAR_image...
pv -tpreb -s $VAR_image_z_size $VAR_SD_images_folder$VAR_image_z | unpigz > $VAR_SD_images_folder$VAR_image

VAR_image_size=$(stat -c%s "$VAR_SD_images_folder$VAR_image")

echo [2/3] Copying image file $VAR_image to SD card \($VAR_SDcard\)...
pv -tpreb -s $VAR_image_size $VAR_SD_images_folder$VAR_image | dd of=$VAR_SDcard;

# Cleaning
echo [3/3] Delete $VAR_image file...
rm $VAR_SD_images_folder$VAR_image

echo Done !
