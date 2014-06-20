#import picamera
import sys
import boto
from boto.s3.key import Key
import time
import ConfigParser
import requests

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
        self.post_url = config.get('local', 'post_url')
        self.conn = self._get_connection()
        self.s3_base_path = self.bucket_name

    def _get_connection(self):
        return boto.connect_s3(self.aws_access_key, 
                               self.aws_secret_access_key)


    def take_picture(self, file_name):
        """
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(5) 
            camera.capture(concat_paths(self.photo_base, file_name))
            camera.stop_preview()
        """
        return file_name

    def send_photo(self, file_name):
        bucket = self.conn.get_bucket(self.bucket_name)
        key = Key(bucket)
        key.key = file_name 
        key.set_contents_from_filename(concat_paths(self.photo_base, file_name))
        return True
   
    def make_file_name(self):
        time_stamp = str(time.time()).split('.')[0]
        return [('%s-%s.jpg' % (self.camera_id, time_stamp)), time_stamp]

    def send_request(self, file_name, time_stamp):
        payload = {
                    'camera_id'    : self.camera_id,
                    'picture_id'   : file_name,
                    's3_base_path' : self.s3_base_path,
                    'time_stamp'   : time_stamp
                }    
        r = requests.post(self.post_url, data=payload)
        print r.text




def main():
    if len(sys.argv) != 2:
        print 'pass in config file'
        print 'Run as:'
        print 'python script.py test.cfg'
        exit(1)
    config_file = sys.argv[1]
    photo_scripter = PhotoScript(config_file)

    file_name, time_stamp = photo_scripter.make_file_name()
    file_name = 'test.jpg'
    photo_scripter.take_picture(file_name)
    photo_scripter.send_photo(file_name)
    photo_scripter.send_request(file_name, time_stamp)


if __name__ == '__main__':
    main()
     
