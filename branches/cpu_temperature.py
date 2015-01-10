#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import subprocess

class Sensor_temperature_cpu(object):  
  
  sensor_name = "CPU temperature"  
  sensor_unit = "ºC"
  sensor_desc = "onboard Raspberry Pi B+"
  
  def get_sensor_value(self):
      #"Returns the temperature in degrees celcius"
      try:
	    s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
	    return float(s.split('=')[1][:-3])
      except:
	    return -99


