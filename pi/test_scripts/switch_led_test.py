#!/usr/bin/python
import RPi.GPIO as GPIO
import time
led_pin = 17
switch_pin = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def main():
    setup()
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(switch_pin, GPIO.IN)
    while True:
        if ( GPIO.input(switch_pin) == False):
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

main()
