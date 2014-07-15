#!/usr/bin/python
import RPi.GPIO as GPIO
import time
sen_pin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def main():
    setup()
    print "starting"
    print read_analog(sen_pin)
    

def read_analog(pin):
    counter = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.OUT)
    while(GPIO.input(pin) == GPIO.LOW):
        counter += 1

    return counter

if __name__ == "__main__":
    main()
