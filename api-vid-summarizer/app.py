import os
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from flask_session import Session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
from model import *
from yt import *
from transcript_model import *

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')
sess = Session()


UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'./test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    #session['uploadFilePath']=destination
    res = summarize_text_model()
    #response="Whatever you wish too return"
    return jsonify(res)

@app.route('/link', methods = ['GET'])
def yt_file_upload():
    args = request.args
    youtubeLink = args.get('youtubeUrl')
    res = yt_model(youtubeLink)
    return jsonify(res)

@app.route('/transcript', methods = ['GET'])
def transcript_generator():
    res = transcript_gen()
    return res

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)
    
CORS(app, expose_headers='Authorization')