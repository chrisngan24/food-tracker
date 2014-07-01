#!/usr/bin/python
import RPi.GPIO as GPIO
import time
pin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def main():
    setup()
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(4)
    GPIO.output(pin, GPIO.LOW)

main()
