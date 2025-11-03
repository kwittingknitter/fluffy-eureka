"""LegislatorsRepository"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from service.models import Legislator


class LegislatorsRepository:
    """Connects to DB and queries Legislator"""

    def __init__(self, db: SQLAlchemy):
        """Initializes LegislatorsRepository"""
        self.db = db

    def get_by_id(self, id: int):
        """Get Legislator by ID or raise error"""
        return self.db.get_or_404(Legislator, id)

    def get_all(self, filters: dict = None):
        """Get all from Legislator"""
        query = self.db.select(Legislator)
        if filters:
            if 'state' in filters and filters['state']:
                query = query.where(
                    func.lower(Legislator.state) == filters['state'].lower()
                )
        return self.db.session.execute(query).scalars().all()
