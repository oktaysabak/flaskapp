import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deneme-anahtar-gizli'
    WTF_CSRF_SECRET_KEY="very very very secret key"