import os
from datetime import datetime


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_SECRET = SECRET_KEY
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = 259200
    
class Dev(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG = True

class Prod(Config):
    DEBUG = False
    DEVELOPMENT = False
    DEBUG = False
