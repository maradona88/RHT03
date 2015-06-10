import sys
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import threading
import datetime

pin_number = 13
sensor = 22

GPIO.setmode(GPIO.BCM)

def get_readings:
	humidity, temperature = Raspberry_Pi_2.read_retry(sensor, pin_number)
	file = open('logfile.txt', 'a')
	if humidity is not None and temperature is not None:
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		print "Time: %s Temp: %.1f Humidity: %.1f\n" % (st, temperature, humidity)
		file.write("%s %.1f %.1f\n" % (st, temperature, humidity))
		file.close()
		time.sleep(60)
	
	
while (True):
	get_readings()
