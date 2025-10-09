""" Flask app file """

import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import Base
from scripts import insert_seed_data


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

default_uri = "mysql+pymysql://{}:{}@{}:3306/{}".format(
    os.getenv('MYSQL_USER', 'root'),
    os.getenv('MYSQL_PASSWORD'),
    os.getenv('MYSQL_HOST', 'localhost'),
    os.getenv('MYSQL_DB', 'service_db'))

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', default_uri)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_ECHO'] = "debug"
app.config['FLASK_DEBUG'] = os.getenv('DEBUG', 'True')
app.logger.setLevel(logging.DEBUG)

db.init_app(app)

# TODO: add check if db and tables exist before below
with app.app_context():
    db.drop_all()
    db.create_all()
    insert_seed_data(db)

from routes import *
