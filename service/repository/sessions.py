"""SessionsRepository"""

from flask_sqlalchemy import SQLAlchemy

from service.models import Session, Legislator
from sqlalchemy import extract, func


class SessionsRepository:
    """Connects to DB and queries Session"""

    def __init__(self, db: SQLAlchemy):
        """Initializes SessionsRepository"""
        self.db = db

    def get_by_id(self, id: int):
        """Get Session by ID or raise error"""
        return self.db.get_or_404(Session, id)

    def get_all(self, filters: dict = None):
        """Get all from Session"""
        query = self.db.select(Session)
        if filters:
            if 'state' in filters and filters['state']:
                query = query.where(Session.legislators.any(func.lower(Legislator.state) == filters['state'].lower()))
            if 'year' in filters and filters['year']:
                query = query.where(extract('year', Session.begin_date) == filters['year'])
        return self.db.session.execute(query).scalars().all()
