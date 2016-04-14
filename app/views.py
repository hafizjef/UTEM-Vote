from flask import render_template, flash, redirect, session
from app import app, socketio
from .forms import LoginForm
from datetime import datetime


voteEnable = True
campaign = 'UTeM 2016'
ccc = 0


@app.route('/')
@app.route('/index')
def index():
    if (voteEnable):
        sdata = {
                    'name': campaign,
                    'voting': voteEnable,
                    'time': datetime.now()
                }
        return render_template("index.html", title='Home', posts=sdata)
    else:
        sdata = {'name': None, 'voting': voteEnable, 'time': datetime.now()}
        return render_template("index.html", title='Home', posts=sdata)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Sign In')


@app.route('/vote')
def vote():
    return render_template('vote.html', title='Vote', vote=voteEnable)


@socketio.on('connect', namespace='/dd')
def test_connect():
    global ccc
    ccc += 1
    socketio.emit('msg', {'data': 'Connected', 'count': ccc}, namespace='/dd')


@socketio.on('disconnect', namespace='/dd')
def test_disconnect():
    global ccc
    ccc -= 1
    socketio.emit('msg', {'data': 'Connected', 'count': ccc}, namespace='/dd')
