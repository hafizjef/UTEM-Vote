class Config(object):
    """Base Config"""
    DEBUG = False
    TESTING = False

    """SQLAlchemy Config"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///engine.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    SECRET_KEY = 'soSecret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///engine.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
