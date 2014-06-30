import picamera
import sys
import boto
from boto.s3.key import Key
import time
import ConfigParser
from photoscript import PhotoScript
import RPi.GPIO as GPIO
import led

def check_sensor(sensor_pin):
    if (GPIO.input(sensor_pin) == False):
        return True
    else:
        return False

def main():
    if len(sys.argv) != 2:
        print 'pass in config file'
        print 'Run as:'
        print 'python script.py test.cfg'
        exit(1)
    config_file = sys.argv[1]
    photo_scripter = PhotoScript(config_file)


    salient_pin = 17
    entrance_pin = 22
    sensor_pin = 27
    current_state = None 
    led.setup()
    GPIO.setup(salient_pin, GPIO.OUT)
    GPIO.setup(entrance_pin, GPIO.OUT)
    GPIO.setup(sensor_pin, GPIO.IN)
    GPIO.output(entrance_pin, GPIO.HIGH)
    while True:
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
     
