#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from cpu_temperature import Cpu_temperature
from time import sleep

class Example(object):
    def run(self):
        print "Hello, world!"
        


if __name__ == '__main__':
  Example().run()
  while 1:  
    print Cpu_temperature().get_temperature()
    sleep(2)

