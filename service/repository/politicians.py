"""PoliticiansRepository"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from service.models import Politician, Legislator


class PoliticiansRepository:
    """Connects to DB and queries Politician"""

    def __init__(self, db: SQLAlchemy):
        """Initialize repository"""
        self.db = db

    def get_by_id(self, id: int):
        """Get a politican by id
        Returns Politican or raises error"""
        response = self.db.get_or_404(Politician, id)
        return response

    def get_all(self, filters: dict = None):
        """Get all from Politician by filters"""
        query = self.db.select(Politician)
        if filters:
            if 'state' in filters and filters['state']:
                query = query.where(Politician.legislators.any(func.lower(Legislator.state) == filters['state'].lower()))
            if 'name' in filters and filters['name']:
                query = query.where(
                    (func.lower(Politician.first_name) == filters['name'].lower()) | (func.lower(Politician.last_name) == filters['name'].lower())
                )
        return self.db.session.execute(query).scalars().all()
