from flask import render_template, flash, redirect, session, url_for
from app import app, db
from .forms import LoginForm
from datetime import datetime


from app.models.appmodels import Admins, Candidate

voteEnable = False
campaign = 'UTeM 2016'


@app.route('/')
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
    return render_template('login.html', title='Admin Login')


@app.route('/vote')
def vote():
    candidates = db.session.query(Candidate).all()
    return render_template('vote.html', title='Vote', vote=voteEnable, users=candidates)

@app.route('/disable')
def disableVote():
    global voteEnable
    voteEnable = False
    flash('Voting is disabled')
    return redirect(url_for('index'))

@app.route('/enable')
def enableVote():
    global voteEnable
    voteEnable = True
    flash('Voting is enabled')
    return redirect(url_for('index'))

@app.route('/admin')
def adminPanel():
    global voteEnable
    global campaign
    return render_template('admin_panel.html', title='Admin Panel', voteStatus=voteEnable, campaign=campaign)