import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = "debug"

    MYSQL_USER = "root"
    DB_SERVER = "localhost"
    MYSQL_DB = "service_db"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"mysql+pymysql://{self.MYSQL_USER}:{os.getenv('MYSQL_PASSWORD')}@{self.DB_SERVER}:3306/{os.getenv('MYSQL_DB')}"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
    TESTING = True

    def __init__(self, uri):
        SQLALCHEMY_DATABASE_URI = uri
