import requests
import time
import json

def test_push_photo(test_url):
    payload = {
            'bucket' : 'food-tracker',
            'time_in'   : str(time.time()),
            'camera_id' : '12345',
            'mode'      : '001',
            'file_name' : '012-1403293585.jpg'

            }
    r = requests.post(test_url + '/api/v1/photo', data=json.dumps(payload)) 

    print r
    
test_push_photo('http://localhost:5000')
