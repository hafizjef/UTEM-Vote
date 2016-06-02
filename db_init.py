from app import db
from app.models.appmodels import Admins
from app.models.appmodels import Candidate
from app.models.appmodels import Vote

from datetime import datetime

# create db
db.drop_all()
db.create_all()

db.session.add(Admins('Admin', 'password', 'admin@website.com'))
#db.session.add(Candidate('Abdullah', 'B031510410', 'FTMK', 3, 2, 'Bendahari'))
db.session.add(Vote(1, datetime.now()))

db.session.commit()
