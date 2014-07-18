from flask import Flask
from flask import request
import json
from photo_scraper import PhotoScraper
from web_scraper import WebScraper 
import r_scraper


TEMP_DIR = 'temp_photo'


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/api/v1/photo', methods=['POST'])
def push_photo():   
    # read request data
    data = json.loads(request.get_data())
    photo_scraper = PhotoScraper(TEMP_DIR)  
    output_file = photo_scraper.get_picture(data['bucket'], data['file_name'])
    classification = r_scraper.classify_photo(output_file)
    camera_id = data['camera_id']
    mode = data['mode']
    date = data['time_in'] 
    web = WebScraper()
    web.post_entry({
        'time_in'  : date,
        'camera_id': camera_id,
        'item_name': classification})
    return 'success'
    

if __name__ == '__main__':
    app.run(debug=True)
