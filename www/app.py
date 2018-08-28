# Imports
from flask import Flask
from flask import render_template
from flask import jsonify
from aux_pro import Process
from database import Database

app = Flask(__name__)
db = Database()
proc = Process()

@app.route('/')
def index():
    samples = jsonify( db.get_last())
    return render_template('index.html', samples= samples)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)


def start_process():
    proc.start_process()
