import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask.ext.socketio import SocketIO

app = Flask(__name__)
# app.config.from_object('instance.config')
app.config.from_object('config.DevConfig')
socketio = SocketIO(app, timeout=1)

from app import views
