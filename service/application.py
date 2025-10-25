"""Application factory"""
import logging 

from flask import Flask

from .configs import DevConfig
from .utils import preprocess

def create_app(config=None):
    if not config:
        config = DevConfig()

    app = Flask(__name__)
    app.config.from_object(config)
    app.logger.log(logging.INFO, 'db uri: ', config.SQLALCHEMY_DATABASE_URI)

    from .models import db
    db.init_app(app)

    with app.app_context():
        # TODO check if tables exist first
        db.drop_all()
        db.create_all()
        _insert_seed_data(db)

    from .routes import route_blueprint
    app.register_blueprint(route_blueprint)

    return app


def _insert_seed_data(db):
    """Inserts seed data into the database, db"""

    politicians, sessions, legislators, committees = preprocess()
    db.session.add_all(politicians)
    db.session.add_all(sessions)
    db.session.add_all(legislators)
    db.session.add_all(committees)
    db.session.commit()
