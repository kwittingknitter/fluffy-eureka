"""PoliticiansRepository"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from service.models import Politician


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

    def search_by_name(self, name: str):
        """Searches for a politican by string (name)
        Returns Politican or None"""
        return self.db.session.execute(
            self.db.select(Politician).where(
                (func.lower(Politician.first_name) == name.lower()) | (func.lower(Politician.last_name) == name.lower()))
        ).scalars().all()

    def get_all(self):
        """Get all from Politician"""
        return self.db.session.execute(self.db.select(Politician)).scalars().all()

    def get_all_by_state(self, state):
        """Get all from Politician by state"""
        # TODO
        return []

