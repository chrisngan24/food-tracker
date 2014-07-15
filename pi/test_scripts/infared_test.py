#!/usr/bin/python
import RPi.GPIO as GPIO
import time
infared_pin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def main():
    setup()
    GPIO.setup(infared_pin, GPIO.IN)
    while True:
        print GPIO.input(infared_pin)
        time.sleep(0.1)

if __name__ == "__main__":
    main()

