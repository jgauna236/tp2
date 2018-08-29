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
    samples = db.get_last_ten()
    return render_template('index.html', samples = samples, refresco = 1)

@app.route("/1/", methods=['GET', 'POST'])
def one():
    samples = db.get_last_ten()/
    return render_template('index.html', samples = samples, refresco = 1)

@app.route("/2/", methods=['GET', 'POST'])
def two():
    samples = db.get_last_ten()
    return render_template('index.html', samples = samples, refresco = 2)

@app.route("/5/", methods=['GET', 'POST'])
def three():
    samples = db.get_last_ten()
    return render_template('index.html', samples = samples, refresco = 5)

@app.route("/10/", methods=['GET', 'POST'])
def ten():
    samples = db.get_last_ten()
    return render_template('index.html', samples = samples, refresco = 10)

@app.route("/30/", methods=['GET', 'POST'])
def thirty():
    samples = db.get_last_ten()
    return render_template('index.html', samples = samples, refresco = 30)


@app.route("/60/", methods=['GET', 'POST'])
def sixty():
    samples = db.get_last_ten()
    return render_template('index.html', samples = samples, refresco = 60)

def start_process():
    proc.start_process()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)


