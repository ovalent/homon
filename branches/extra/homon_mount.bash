#!/bin/bash

VAR_mount_folder=/home/oli/raspberry/oli-pi

#sshfs pi@192.168.0.44:/home/pi/homon /home/oli/homon_oli-pi/
#sshfs -o idmap=user -o gid=`id --group` pi@192.168.0.44:/home/pi/ /home/oli/raspberry/oli-pi
sshfs pi@192.168.0.44:/home/pi/ $VAR_mount_folder
echo pi@oli-pi home mounted in $VAR_mount_folder.

