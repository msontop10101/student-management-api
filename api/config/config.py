import os
from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY','secret')

class DevConfig:
    DEBUG=config('DEBUG',cast=bool)

class TestConfig:
    pass

class ProdConfig:
    pass

config_dist={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}