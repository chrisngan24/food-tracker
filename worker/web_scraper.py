import os
import requests
import json

class WebScraper:
    def __init__(self):
        self.base_url = os.getenv('APP_URL')

    def post_request(self, url, data):
        full_url = '%s/%s' % (self.base_url, url)
        r = requests.post(full_url, data=json.dumps(data))


    def post_entry(self, data):
        self.post_request('api/v1/add_entry', data)


         
        
