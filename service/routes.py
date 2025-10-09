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

@app.route('/politicians/<string:name>')
def get_politician(name):
    """Search for politician by name"""
    response = db.session.execute(
        db.select(Politician).where(
            (Politician.first_name.like(name)) | (Politician.last_name.like(name))
        )).scalars().all()
    if len(response) > 0 and len(response) == 1:
        resp_dict = PoliticianScheme().dump(response[0])
        return resp_dict
    elif len(response) == 0:
        return jsonify({"response": []})
    return jsonify({
        "response": [PoliticianScheme().dump(r) for r in response]
    })

# TODO: fix issue with datetime in leg, sessions

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

@app.route('/sessions', defaults={'id': None})
@app.route('/sessions/<int:id>')
def get_sessions(id: None):
    """Get info about one session by id or all sessions"""
    response = None
    if id:
        response = db.get_or_404(Session, id)
        return SessionScheme().dump(response)
    response = db.session.execute(db.select(Session)).scalars().all()
    return jsonify({
        "response": [SessionScheme().dump(r) for r in response]
    })

