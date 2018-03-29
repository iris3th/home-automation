#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [4, 22, 6, 26]

# loop through pins and set mode and state to 'low'

for i in pinList: 
  GPIO.setup(i, GPIO.OUT) 
  GPIO.output(i, GPIO.LOW)

# time to sleep between operations in the main loop

SleepTimeL = 2

# switch relays on and off

try:
  GPIO.output(4, GPIO.HIGH)
  print "1 ON"
  time.sleep(SleepTimeL); 
  GPIO.output(4, GPIO.LOW)
  print "1 OFF"
  GPIO.output(22, GPIO.HIGH)
  print "2 ON"
  time.sleep(SleepTimeL); 
  GPIO.output(22, GPIO.LOW)
  print "2 OFF"
  GPIO.output(6, GPIO.HIGH)
  print "3 ON"
  time.sleep(SleepTimeL); 
  GPIO.output(6, GPIO.LOW)
  print "3 OFF"
  GPIO.output(26, GPIO.HIGH)
  print "4 ON"
  time.sleep(SleepTimeL); 
  GPIO.output(26, GPIO.LOW)
  print "4 OFF"
except KeyboardInterrupt:  
  print " Quit" 

 # do cleanup
GPIO.cleanup()
