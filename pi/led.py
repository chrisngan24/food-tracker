import RPi.GPIO as GPIO
import time
led_pin = 17
switch_pin = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def flash_led(led_pin):
    for i in range(0,1):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.4)

def toggle_light(led_pin, state):
    GPIO.output(led_pin, state)

def test():
    setup()
    GPIO.setup(led_pin, GPIO.OUT)
    flash_led(led_pin)
