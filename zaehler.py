#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pressed = False

def btn_callback(channel):
	global pressed
	if pressed is False:
		# hier kommt der SQL INSERT hin
		print('Button pressed on %s'%channel)
		pressed = True
	else:
		print('Button released on %s'%channel)
		pressed = False

GPIO.add_event_detect(18, GPIO.BOTH, callback=btn_callback, bouncetime=300)

try:
	print("Waiting...")
	GPIO.wait_for_edge(24, GPIO.RISING)

except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()

