"""CommitteesRepository"""

from flask_sqlalchemy import SQLAlchemy

from models import Committee


class CommitteesRepository:
    """Connects to DB and queries Committee"""

    def __init__(self, db: SQLAlchemy):
        """Initializes CommitteesRepository"""
        self.db = db

    def get_by_id(self, id: int):
        """Get Committee by ID or raise error"""
        return self.db.get_or_404(Committee, id)

    def get_all(self):
        """Get all Committees"""
        return self.db.session.execute(self.db.select(Committee)).scalars().all()
