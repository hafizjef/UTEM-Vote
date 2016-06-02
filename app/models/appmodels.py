from app import db


class Admins(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return self.username


class Candidate(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, unique=True)
    studentId = db.Column(db.String(10), unique=True)
    faculty = db.Column(db.String(5), nullable=False)
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    position = db.Column(db.String)
    electionCode = db.Column(db.String)
    count = db.Column(db.Integer)

    def __init__(self, name, studentId, faculty, year, semester, position, electionCode, count):
        self.name = name
        self.studentId = studentId
        self.faculty = faculty
        self.year = year
        self.semester = semester
        self.position = position
        self.electionCode = electionCode
        self.count = count

    def __repr__(self):
        return self.name


class Vote(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    candidateId = db.Column(db.Integer)
    voteTime = db.Column(db.DateTime)

    def __init__(self, candidateId, voteTime):
        self.candidateId = candidateId
        self.voteTime = voteTime

    def __repr__(self):
        return self.name