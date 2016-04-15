from flask import render_template, flash, redirect, session
from app import app, db
from .forms import LoginForm
from datetime import datetime


from app.models.appmodels import Admins

voteEnable = True
campaign = 'UTeM 2016'


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
    contestants = db.session.query(Admins).all()
    return render_template('vote.html', title='Vote', vote=voteEnable, users=contestants)
