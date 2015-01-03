#!/bin/bash
VAR_mount_folder=/home/oli/raspberry/oli-pi
fusermount -u $VAR_mount_folder
echo pi@oli-pi folder $VAR_mount_folder UNmounted. 
