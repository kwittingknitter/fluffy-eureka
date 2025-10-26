""" Routes for Flask app """

from flask import jsonify, Blueprint

from .schemas import PoliticianScheme, LegislatorScheme, SessionScheme
from .repository import politicians_repo, legislators_repo, sessions_repo


route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def index():
    """Pong back"""
    return "Pong!"

@route_blueprint.route('/politicians/<int:id>')
def get_politician_by_id(id: int):
    """Get info about a politician"""
    politicians = politicians_repo.get_by_id(id)
    response = PoliticianScheme().dump(politicians)
    return response

@route_blueprint.route('/politicians')
def get_all_politicians():
    """Get info about all politicians"""
    politicians = politicians_repo.get_all()
    return jsonify({
        "response": [PoliticianScheme().dump(politician) for politician in politicians]
    })

@route_blueprint.route('/politicians/state/<string:state>')
def get_all_politicians_by_state(state):
    """Get info about all politicians filtered by state"""
    politicians = politicians_repo.get_all_by_state()
    return jsonify({
        "response": [PoliticianScheme().dump(politician) for politician in politicians]
    })

@route_blueprint.route('/politicians/<string:name>')
def get_politician(name):
    """Search for politician by name"""
    politicians = politicians_repo.search_by_name(name)
    if len(politicians) == 0:
        return jsonify({"response": []})
    return jsonify({
        "response": [PoliticianScheme().dump(politician) for politician in politicians]
    })

@route_blueprint.route('/legislators/<int:id>')
def get_legislator_by_id(id: int):
    """Get info about one legislator by id"""
    legislator = legislators_repo.get_by_id(id)
    return LegislatorScheme().dump(legislator)

@route_blueprint.route('/legislators')
def get_legislators():
    """Get all state legislators"""
    legislators = legislators_repo.get_all()
    return jsonify({
        "response": [LegislatorScheme().dump(legislator) for legislator in legislators]
    })

@route_blueprint.route('/legislators/state/<string:state>')
def get_legislators_by_state(state: str):
    """Get all legislators by state"""
    legislators = legislators_repo.get_by_state(state)
    return jsonify({
        "response": [LegislatorScheme().dump(legislator) for legislator in legislators]
    })

@route_blueprint.route('/sessions/<int:id>')
def get_session_by_id(id: int):
    """Get session by ID"""
    session = sessions_repo.get_by_id(id)
    return SessionScheme().dump(session)

@route_blueprint.route('/sessions')
def get_sessions():
    """Get all sessions"""
    sessions = sessions_repo.get_all()
    return jsonify({
        "response": [SessionScheme().dump(session) for session in sessions]
    })

@route_blueprint.route('/sessions/state/<string:state>')
def get_sessions_by_state(state: str):
    """Get all sessions by state"""
    sessions = sessions_repo.get_all_by_state(state)
    return jsonify({
        "response": [SessionScheme().dump(session) for session in sessions]
    })
