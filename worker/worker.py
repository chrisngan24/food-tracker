from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

@app.route('/api/v1/photo', methods=['POST'])
def push_photo():   
    # read request data
    camera_id = request.form['camera_id']
    picture_id = request.form['picture_id'] 
    s3_base_path = request.form['s3_base_path']
    time_stamp = request.form['time_stamp']
    return '200'
    


    

if __name__ == '__main__':
    app.run(debug=True)
