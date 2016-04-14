class Config(object):
    ''' Base Config '''
    DEBUG = False
    TESTING = False

    ''' SQLAlchemy Config '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///engine.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///engine.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True