#!.venv/bin/python
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'you-will-never-guess'
    WTF_CSRF_ENABLED = False
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestConfig(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'you-will-never-guess'
    WTF_CSRF_ENABLED = False
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS=False