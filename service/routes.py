""" Routes for Flask app """

from flask import jsonify

from app import app
from schemas import PoliticianScheme, LegislatorScheme, SessionScheme
from repository import politicians_repo, legislators_repo, sessions_repo


@app.route('/')
def index():
    """Pong back"""
    return "Pong!"

@app.route('/politicians/<int:id>')
def get_politician_by_id(id: int):
    """Get info about a politician who's served in the OR state legislature"""
    politicians = politicians_repo.get_by_id(id)
    response = PoliticianScheme().dump(politicians)
    return response

@app.route('/politicians')
def get_all_politicians():
    """Get info about all politicians who've served in the OR state legislature"""
    politicians = politicians_repo.get_all()
    return jsonify({
        "response": [PoliticianScheme().dump(politician) for politician in politicians]
    })

@app.route('/politicians/<string:name>')
def get_politician(name):
    """Search for politician by name"""
    politicians = politicians_repo.search_by_name(name)
    if len(politicians) == 0:
        return jsonify({"response": []})
    return jsonify({
        "response": [PoliticianScheme().dump(politician) for politician in politicians]
    })

@app.route('/legislators/<int:id>')
def get_legislator_by_id(id: int):
    """Get info about one legislator by id"""
    legislator = legislators_repo.get_by_id(id)
    return LegislatorScheme().dump(legislator)

@app.route('/legislators')
def get_legislators():
    """Get all OR state legislators"""
    legislators = legislators_repo.get_all()
    return jsonify({
        "response": [LegislatorScheme().dump(legislator) for legislator in legislators]
    })

@app.route('/sessions/<int:id>')
def get_session_by_id(id: int):
    """Get session by ID"""
    session = sessions_repo.get_by_id(id)
    return SessionScheme().dump(session)

@app.route('/sessions')
def get_sessions():
    """Get all sessions"""
    sessions = sessions_repo.get_all()
    return jsonify({
        "response": [SessionScheme().dump(session) for session in sessions]
    })
