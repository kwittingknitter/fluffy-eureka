"""Flask app configs"""

import os


class Config(object):
    """Config object"""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    DB_NAME = "service_db"
    DB_HOST= "localhost"


class DevConfig(Config):
    """Dev config object"""
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = "debug"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST', self.DB_HOST)}:5432/{os.getenv('DB_NAME', self.DB_NAME)}"


class TestConfig(Config):
    """Test config object"""
    SQLALCHEMY_DATABASE_URI = ''
    TESTING = True
