from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Login form class"""
    username = StringField('user', validators=[DataRequired()])
    password = StringField('pass', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
