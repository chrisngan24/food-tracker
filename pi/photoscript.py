import picamera
import sys
import boto
from boto.s3.key import Key
import time
import ConfigParser
import requests
import json


def parse_config_file(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file))
    return config

def concat_paths(base, fil):
    return '%s/%s' % (base, fil)


class PhotoScript:
    def __init__(self, config_file):
        config = parse_config_file(config_file) 
        self.aws_access_key = config.get('s3', 'aws_access_key')  
        self.aws_secret_access_key = config.get('s3', 'aws_secret_access_key')  
        self.bucket_name = config.get('s3', 'bucket')
        self.camera_id = config.get('local', 'camera_id')
        self.photo_base = config.get('local', 'photo_base')
        self.conn = self._get_connection()
        self.url = config.get('url', 'url')

    def _get_connection(self):
        return boto.connect_s3(self.aws_access_key, 
                               self.aws_secret_access_key)


    def take_picture(self, file_name):
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(0.5) 
            camera.capture(concat_paths(self.photo_base, file_name))
            camera.stop_preview()
        return file_name

    def send_photo(self, file_name):
        bucket = self.conn.get_bucket(self.bucket_name)
        key = Key(bucket)
        key.key = file_name 
        key.set_contents_from_filename(concat_paths(self.photo_base, file_name))
        return True
   
    def make_file_name(self):
        return ('%s-%s.jpg' % (self.camera_id, str(time.time()).split('.')[0])) 
    def send_request(self, url, payload):
        r = requests.post(url, data=json.dumps(payload))
        print r



