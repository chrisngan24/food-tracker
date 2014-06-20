import picamera
import boto
from boto.s3.key import Key
import time

BUCKET = 's3://food-tracker'
def take_picture(file_name):

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(5) 
	camera.capture(file_name)
        camera.stop_preview()
    return file_name
    

def send_photo(conn, file_name, output_key):
    bucket = conn.get_bucket(BUCKET) 
    key = Key(bucket)
    k.key = output_key
    key.set_contents_from_filename(file_name)

def main():
    file_name = 'test.jpg'
    take_picture(file_name)
    conn = boto.connect_s3('123', '123')
    send_photo(conn, file_name, 'test')

if __name__ == '__main__':
    main()
     
