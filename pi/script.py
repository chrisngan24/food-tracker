#import picamera
import sys
import boto
from boto.s3.key import Key
import time
import ConfigParser

BUCKET = 'food-tracker'
PHOTO_STORAGE = 'photos'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

def take_picture(file_name):
    """
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(5) 
	camera.capture(file_name)
        camera.stop_preview()
        """
    return file_name
    
def get_config(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file))
    return config



def send_photo(conn, file_name, output_key):
    bucket = conn.get_bucket(BUCKET) 
    key = Key(bucket)
    key.key = output_key
    key.set_contents_from_filename(file_name)

def main():
    config_file = sys.argv[1]
    config = get_config(config_file)
    file_name = PHOTO_STORAGE + '/test.jpg'
    take_picture(file_name)
    conn = boto.connect_s3(config.get('s3', 'aws_access_key'), 
                            config.get('s3', 'aws_secret_access_key'))
    send_photo(conn, file_name, 'test.jpg')

if __name__ == '__main__':
    main()
     
