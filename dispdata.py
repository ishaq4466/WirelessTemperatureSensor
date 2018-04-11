# ==========DISPLAYING SENSOR DATA TO THE CONSOLE=================

#This script will fetch the sensor data from the sensor and display it
#on the console screen github/HarryGoodwin(original source code)
#import os
import time
import datetime
import glob
from time import strftime


#loading gpio & therm kernel by using the modprobe linux program

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

#enter the dir path in the 'temp_sensor' variable 
#for the file in which temperature value is
#recorded checkout in following directory-> '/sys/bus/w1/devices/28-00000622fd44/w1_slave'

temp_sensor = '/home/ec2-user/mydir/temp'


#tempRead() opens the file in which temperature value in stored
#and convert it into floating data value and return it to the 
#temp variable in the below loop
def tempRead():
	t = open(temp_sensor, 'r')
	lines = t.readlines()
	t.close()
        temp_output = lines[1].find('t=')
	if temp_output != -1:
		temp_string = lines[1].strip()[temp_output+2:]
		temp_c = float(temp_string)/1000.0
		return round(temp_c,1)


#while loop just print the temperature and print it along with the
#date by using 'time' library

while True:
	temp = tempRead()
	print temp
	datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
      print 'Time: '+datetimeWrite
	#time.sleep(3)
	break