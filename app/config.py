import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'qwerrytuyu'
    SQLALCHEMY_DATABASE_URI = "postgres://ijeluwvlytupum:9ff5dfe8bbebe071e23eb32f7368c49bfdf7c9225ff11d815a62efa8d886b972@ec2-35-153-12-59.compute-1.amazonaws.com:5432/dcbquc2s74thpe"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
