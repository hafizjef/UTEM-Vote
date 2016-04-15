from flask import render_template, flash, redirect, session
from app import app, socketio


@app.route('/endpoint/<int:version>')
def twillio(version):
    return 'Twillio api here ' + str(version)
