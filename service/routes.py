""" Routes for Flask app """

from flask import jsonify, Blueprint, request

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
    """Get info about all politicians, filterable by state and name"""
    filters = {
        'state': request.args.get('state'),
        'name': request.args.get('name')
    }
    politicians = []
    if filters['name'] or filters['state']:
        politicians = politicians_repo.get_all(filters)
    else:
        politicians = politicians_repo.get_all()
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
    """Get all state legislators, filterable by state"""
    filters = {
        'state': request.args.get('state')
    }
    legislators = legislators_repo.get_all(filters)
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
    filters = {
        'state': request.args.get('state'),
        'year': request.args.get('year'),
    }
    sessions = sessions_repo.get_all(filters)
    return jsonify({
        "response": [SessionScheme().dump(session) for session in sessions]
    })
