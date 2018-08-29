# Imports
from flask import Flask
from flask import render_template
from flask import jsonify
from models import Samples
from aux_pro import Process
from database import Database

import time

samples = Samples()
app = Flask(__name__)
db = Database()
proc = Process()

@app.route('/')
def index():
    proc.start_process()
    time.sleep(10)
    samples = db.get_last()
    return render_template('index.html', samples = jsonify(samples))

def start_process():
    proc.start_process()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)


