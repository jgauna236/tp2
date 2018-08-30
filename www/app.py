# Imports
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
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
    promedios = db.get_promedio()
<<<<<<< HEAD
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 10)
=======
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 60)

@app.route('/stop', methods = ["GET"])
def stop():
    data = pro.stop_process()
    return jsonify({"status": data})
>>>>>>> bb1024c722ea2b262a67231588adeadd13a9f6be

@app.route("/actualizar", methods=["POST"])
def actualizar():
    data = request.form
    refresco = data["refresco"]
    return redirect("/"+refresco)

@app.route("/1", methods=['GET', 'POST'])
def one():
    samples = db.get_last_ten()
    promedios = db.get_promedio()
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 1)

@app.route("/2", methods=['GET', 'POST'])
def two():
    samples = db.get_last_ten()
    promedios = db.get_promedio()
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 2)

@app.route("/5", methods=['GET', 'POST'])
def three():
    samples = db.get_last_ten()
    promedios = db.get_promedio()
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 5)

@app.route("/10", methods=['GET', 'POST'])
def ten():
    samples = db.get_last_ten()
    promedios = db.get_promedio()
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 10)

@app.route("/30", methods=['GET', 'POST'])
def thirty():
    samples = db.get_last_ten()
    promedios = db.get_promedio()
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 30)


@app.route("/60", methods=['GET', 'POST'])
def sixty():
    samples = db.get_last_ten()
    promedios = db.get_promedio()
    return render_template('index.html', samples = samples, promedios = promedios, refresco = 60)

def start_process():
    proc.start_process()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
