"""Flask app configs"""

import os


class Config(object):
    """Config object"""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    DB_SERVER = "localhost"


class DevConfig(Config):
    """Dev config object"""
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = "debug"

    MYSQL_USER = "root"
    MYSQL_DB = "service_db"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"mysql+pymysql://{self.MYSQL_USER}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST', self.DB_SERVER)}:3306/{os.getenv('MYSQL_DB')}"


class TestConfig(Config):
    """Test config object"""
    SQLALCHEMY_DATABASE_URI = ''
    TESTING = True
