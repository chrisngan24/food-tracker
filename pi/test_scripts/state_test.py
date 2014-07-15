#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
#pin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def main(pin0, pin1):
    setup()
    GPIO.setup(pin0, GPIO.IN)
    GPIO.setup(pin1, GPIO.IN)

    while (True):
        print 'pin %s: %s    pin %s: %s' % (pin0, GPIO.input(pin0), pin1, GPIO.input(pin1)) 
if __name__ == '__main__':
    pin0 = int(sys.argv[1])
    pin1 = int(sys.argv[2])
    
    main(pin0, pin1)
