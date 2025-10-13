"""SessionsRepository"""

from flask_sqlalchemy import SQLAlchemy

from models import Session


class SessionsRepository:
    """Connects to DB and queries Session"""

    def __init__(self, db: SQLAlchemy):
        """Initializes SessionsRepository"""
        self.db = db

    def get_by_id(self, id: int):
        """Get Session by ID or raise error"""
        return self.db.get_or_404(Session, id)

    def get_all(self):
        """Get all from Session"""
        return self.db.session.execute(self.db.select(Session)).scalars().all()
