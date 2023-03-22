import os
from decouple import config

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY','secret')
    SQLALCHEMY_TRACK_MODIFICATION=False

class DevConfig:
    DEBUG=config('FLASK_DEBUG',cast=bool)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')

class TestConfig:
    pass

class ProdConfig:
    pass

config_dist={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}