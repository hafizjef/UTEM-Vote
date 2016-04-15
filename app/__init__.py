import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask.ext.socketio import SocketIO
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object('instance.config')
app.config.from_object('config.DevConfig')
socketio = SocketIO(app)
db = SQLAlchemy(app)

from app.models import appmodels

from app.views import mainviews
from app.views import events
from app.api import endpoints
