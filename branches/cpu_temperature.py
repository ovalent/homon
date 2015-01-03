#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import subprocess
#import os

class Cpu_temperature(object):  
  def get_temperature(self):
      #"Returns the temperature in degrees C"
      try:
	  s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
	  return float(s.split('=')[1][:-3])
      except:
	  return -99



#print 'Temperature in C: ' +str(get_temperature())