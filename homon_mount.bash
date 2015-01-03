#!/bin/bash

#sshfs pi@192.168.0.44:/home/pi/homon /home/oli/homon_oli-pi/
#sshfs -o idmap=user -o gid=`id --group` pi@192.168.0.44:/home/pi/ /home/oli/raspberry/oli-pi
sshfs pi@192.168.0.44:/home/pi/ /home/oli/raspberry/oli-pi

