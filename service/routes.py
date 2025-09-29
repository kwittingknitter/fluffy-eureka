""" Routes for Flask app """

from flask import jsonify

from app import app, db
from models import *
from schemas import *


@app.route('/')
def index():
    """Pong back"""
    return "Pong!"


@app.route('/politicians', defaults={'id': None})
@app.route('/politicians/<int:id>')
def get_politicians(id: None):
    """Get info about one or all people who've served in the OR state legislature"""
    response = None
    if id:
        response = db.get_or_404(Politician, id)
        resp_dict = PoliticianScheme().dump(response)
        return resp_dict
    response = db.session.execute(db.select(Politician)).scalars().all()
    return jsonify({
        "response": [PoliticianScheme().dump(r) for r in response]
    })


# TODO: fix issue with datetime in leg
@app.route('/legislators', defaults={'id': None})
@app.route('/legislators/<int:id>')
def get_legislators(id: None):
    """Get info about one legislator by id or all legislators"""
    response = None
    if id:
        response = db.get_or_404(Legislator, id)
        return LegislatorScheme().dump(response)
    response = db.session.execute(db.select(Legislator)).scalars().all()
    return jsonify({
        "response": [LegislatorScheme().dump(r) for r in response]
    })

# TODO: allow querying sessions
# TODO: allow query politician by name
# TODO: show legislator info when querying politician
