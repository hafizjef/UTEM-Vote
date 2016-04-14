from app import db
from app.models.appmodels import Admins

# create db
db.create_all()

db.session.add(Admins('test', 'password'))

db.session.commit()