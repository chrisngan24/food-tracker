import picamera
import sys
import boto
from boto.s3.key import Key
import time
import ConfigParser
from photoscript import PhotoScript
import RPi.GPIO as GPIO
import led

INPUT_STATE = 1
OUTPUT_STATE = 0
def check_sensor(sensor_pin):
    if (GPIO.input(sensor_pin) == False):
        return True
    else:
        return False

def check_state(entrance_pin, exit_pin, current_state):
    if (GPIO.input(entrance_pin) == False):
        return INPUT_STATE # entrance state 
    if (GPIO.input(exit_pin) == False):
        return OUTPUT_STATE # exit state 
    return current_state

def enable_state(entrance_pin, exit_pin, state):
    if state == INPUT_STATE:
        GPIO.output(entrance_pin, GPIO.HIGH)
        GPIO.output(exit_pin, GPIO.LOW)
    if state == INPUT_STATE:
        GPIO.output(exit_pin, GPIO.HIGH)
        GPIO.output(entrance_pin, GPIO.LOW)



def main():
    if len(sys.argv) != 2:
        print 'pass in config file'
        print 'Run as:'
        print 'python script.py test.cfg'
        exit(1)
    config_file = sys.argv[1]
    photo_scripter = PhotoScript(config_file)


    salient_pin = 27
    entrance_pin = 17
    exit_pin = 22 
    input_pin = 18
    output_pin = 23 
    sensor_pin = 24 
    current_state = None 
    led.setup()
    GPIO.setup(salient_pin, GPIO.OUT)
    GPIO.setup(entrance_pin, GPIO.OUT)
    GPIO.setup(exit_pin, GPIO.OUT)
    GPIO.setup(sensor_pin, GPIO.IN)
    GPIO.setup(input_pin, GPIO.IN)
    GPIO.setup(output_pin, GPIO.IN)

    while True:
        current_state = check_state(input_pin, 
                                    output_pin, 
                                    current_state)
        enable_state(entrance_pin, exit_pin, current_state)
        if check_sensor(sensor_pin):
            print GPIO.input(sensor_pin)
            file_name = photo_scripter.make_file_name()
            photo_scripter.take_picture(file_name)
            led.flash_led(salient_pin)
            photo_scripter.send_photo(file_name)
            time.sleep(0.2)
        time.sleep(0.2)

   
if __name__ == '__main__':
    main()
     
