import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask.ext.socketio import SocketIO
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
 

app = Flask(__name__)
# app.config.from_object('instance.config')
app.config.from_object('config.DevConfig')
socketio = SocketIO(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

from app.models import appmodels

from app.views import mainviews
from app.views import events
from app.api import endpoints
