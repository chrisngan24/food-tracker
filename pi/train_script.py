import picamera
import os
import sys
import boto
from boto.s3.key import Key
import time
import ConfigParser
from photoscript import PhotoScript

def parse_config_file(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file))
    return config

def concat_paths(base, fil):
    return '%s/%s' % (base, fil)


def main():
    if len(sys.argv) != 4:
        print 'pass in config file'
        print 'Run as:'
        print 'python script.py test.cfg carrot pic_count'
        exit(1)
    config_file = sys.argv[1]
    photo_scripter = PhotoScript(config_file)
    
    classif = sys.argv[2]
    pic_count = int(sys.argv[3])
    create_path(concat_paths(photo_scripter.photo_base, classif))
    time.sleep(5)
    for i in range(0, pic_count):
        file_name = '%s/%s' % (classif, photo_scripter.make_file_name())
        photo_scripter.take_picture(file_name)
        #photo_scripter.send_photo(file_name)
        time.sleep(0.1)

def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
main()
    


    
    



