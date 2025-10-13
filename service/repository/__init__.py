"""Initialize and export repositories"""

from service.models import db

from .legislators import LegislatorsRepository
from .politicians import PoliticiansRepository
from .committees import CommitteesRepository
from .sessions import SessionsRepository

legislators_repo = LegislatorsRepository(db)
politicians_repo = PoliticiansRepository(db)
committees_repo = CommitteesRepository(db)
sessions_repo = SessionsRepository(db)
