import boto
from boto.s3.key import Key
import os
import util

class PhotoScraper:
    def __init__(self, temp_dir):
        self.aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.conn = self.get_connection()
        util.create_path(temp_dir)
        self.temp_dir = temp_dir

    def get_connection(self):
        return boto.connect_s3(self.aws_access_key, 
                               self.aws_secret_access_key)

    def get_picture(self, bucket_name, key_name):
        bucket = self.conn.get_bucket(bucket_name)
        key = bucket.get_key(key_name)
        output_file = '%s/%s' % (self.temp_dir, key_name)
        key.get_contents_to_filename(output_file)
        return output_file
    

