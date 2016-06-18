from flask import Flask, session, request, flash, url_for, redirect, render_template, abort ,g
from app import app, db, login_manager
from .forms import LoginForm
from datetime import datetime

from flask.ext.login import login_user , logout_user , current_user , login_required

from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from app.models.appmodels import Admins, Candidate

voteEnable = False
campaign = 'UTeM 2016'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Page Not Found'), 404


@login_manager.user_loader
def load_user(id):
    return Admins.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def index():
    format = "%a %d %b %Y %H:%M:%S"
    timed = datetime.today().strftime(format)
    if (voteEnable):
        sdata = {
            'name': campaign,
            'voting': voteEnable,
            'time': timed
        }
        return render_template("index.html", title='Home', posts=sdata)
    else:
        sdata = {'name': None, 'voting': voteEnable, 'time': timed}
        return render_template('index.html', title='Home', posts=sdata)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('adminPanel'))
        else:
            return render_template('login.html')
 
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = Admins.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('adminPanel'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 


@app.route('/vote')
def vote():
    candidates = db.session.query(Candidate).all()
    return render_template('vote.html', title='Vote', vote=voteEnable, users=candidates)

@app.route('/disable')
@login_required
def disableVote():
    global voteEnable
    voteEnable = False
    flash('Voting is disabled')
    return redirect(url_for('adminPanel'))

@app.route('/enable')
@login_required
def enableVote():
    global voteEnable
    voteEnable = True
    flash('Voting is enabled')
    return redirect(url_for('adminPanel'))

@app.route('/admin')
@login_required
def adminPanel():
    global voteEnable
    global campaign
    candidates = db.session.query(Candidate).all()

    return render_template('admin_panel.html', title='Admin Panel', voteStatus=voteEnable, campaign=campaign, users=candidates)

@app.route('/updatecamp', methods=['POST'])
def updateCampaign():
    global campaign
    campaign = request.form['campaignName']
    flash('Campaign Name changed succesfully')
    return redirect(url_for('adminPanel'))

@app.route('/addcandidate', methods=['POST'])
def addCandidate():
    name = str.title(request.form['name'])
    userid = (request.form['userid']).upper()
    faculty = request.form['faculty']
    position = request.form['position']
    year = request.form['year']
    semester = request.form['semester']

    rows = db.session.query(Candidate).count() + 1
    code = str(rows).zfill(3)

    db.session.add(Candidate(name, userid, faculty, int(year), int(semester), position, code, 0))
    try:
        db.session.commit()
        return redirect(url_for('adminPanel'))
    except IntegrityError as e:
        flash('Error existed')
        return redirect(url_for('adminPanel'))
    else:
        pass
    finally:
        pass

@app.route('/editcandidate', methods=['POST'])
def editCandidate():
    uid = int(request.form['id'])
    name = str.title(request.form['name'])
    userid = (request.form['userid']).upper()
    faculty = request.form['faculty']
    position = request.form['position']
    year = request.form['year']
    semester = request.form['semester']
    count = request.form['count']

    if (len(userid) != 10):
        flash('Matric Number incorrect')
        return redirect(url_for('adminPanel'))

    update = db.session.query(Candidate).get(uid)
    update.name = name
    update.studentId = userid
    update.faculty = faculty
    update.position = position
    update.year = year
    update.semester = semester
    update.count = count

    db.session.commit()
    return redirect(url_for('adminPanel'))


@app.route('/delcandidate', methods=['POST'])
def deleteCandidate():
    userid = request.form['userid']
    name = Candidate.query.filter(Candidate.id==userid).all()
    Candidate.query.filter(Candidate.id==userid).delete()
    flash('User ' + str(name[0]) + ' deleted!')
    db.session.commit()
    return redirect(url_for('adminPanel'))

@app.route('/results')
def viewResult():
    candidates = db.session.query(Candidate).all()
    return render_template('results.html', title='Results', voteStatus=voteEnable, users=candidates, campaign=campaign)