from app import db


class Admins(db.Model):

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username


class Contestant(db.Model):

    __tablename__ = "contestant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    faculty = db.Column(db.String, nullable=False)

    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

    def __repr__(self):
        return self.name