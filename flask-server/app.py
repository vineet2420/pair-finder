#!/usr/bin/python3
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*")

#sys.path.append('/home/ubuntu/flaskenv/pair-finder/flask-server/venv/lib/python3.6/site-packages/')

@app.route("/")
def hello_world():
    return "<p>Server is up!</p>"

from auth import *
from activity import *

if __name__ == "__main__":
    #app.run(debug=True, port=8000)
    socket.run(app, debug=True, port=8080)