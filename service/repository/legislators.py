"""LegislatorsRepository"""

from flask_sqlalchemy import SQLAlchemy

from service.models import Legislator


class LegislatorsRepository:
    """Connects to DB and queries Legislator"""

    def __init__(self, db: SQLAlchemy):
        """Initializes LegislatorsRepository"""
        self.db = db

    def get_by_id(self, id: int):
        """Get Legislator by ID or raise error"""
        return self.db.get_or_404(Legislator, id)

    def get_all(self):
        """Get all from Legislator"""
        return self.db.session.execute(self.db.select(Legislator)).scalars().all()

    def get_by_state(self, state: str):
        """Get Legislator by state"""
        return self.db.session.execute(self.db.select(Legislator).where(Legislator.state == state)).scalars().all()
