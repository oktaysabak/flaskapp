import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deneme-anahtar-gizli'

    #db
    path = 'sqlite:///' + os.path.join(BASEDIR,'database.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
