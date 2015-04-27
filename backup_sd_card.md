# Introduction #

How to backup Raspberry Pi's SD card.


# Details #

  1. Extract the SD card from your Raspberry Pi and plug it into a linux computer (USB). We assume that the SD card is now identified in /dev/sdb.
  1. Execute the script [back\_sd.bash](https://code.google.com/p/homon/source/browse/branches/extra/backup_sd.bash) (adjust path values inside script variables).

SD backups compressed and stored in folder ../raspberry/sd\_images/

To restore an SD image backup: uncompress the image file and execute the command:
```
sudo dd if=~/raspberry/sd_images/sdimage_<date>.img of=/dev/sdb
```