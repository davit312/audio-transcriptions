import sys
import os

from flask import Flask, render_template, request

import backend

import os

PORT = 8080

RECORDS_PATH = '.' if len(sys.argv) < 2 else sys.argv[1]

if not os.path.isabs(RECORDS_PATH):
    RECORDS_PATH = os.path.normpath(os.path.join(os.getcwd(), RECORDS_PATH))

app = Flask(__name__, static_url_path='', static_folder=RECORDS_PATH,)



@app.route("/", methods = ["GET"])
def list_records():
    return render_template('index.html', records = backend.get_records(RECORDS_PATH))

@app.route('/', methods = ["POST"])
def set_record():
    backend.post_records(RECORDS_PATH, request.get_json())
    return {}, 200

app.run(port=PORT)