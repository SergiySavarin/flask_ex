#!.venv/bin/python
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'you-will-never-guess'
    WTF_CSRF_ENABLED = False
    SECURITY_PASSWORD_SALT = 'my_precious_two'
