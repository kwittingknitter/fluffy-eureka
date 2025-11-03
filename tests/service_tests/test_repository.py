'''
Unit tests for the Flask service repositories
'''


import unittest

from unittest.mock import MagicMock

from service.models import Committee, Legislator, Politician, Session
from service.repository import CommitteesRepository, LegislatorsRepository,\
    PoliticiansRepository, SessionsRepository


class TestRepository(unittest.TestCase):
    """
    Unit tests for Flask service repositories
    """
    committees_repository = None
    sessions_repository = None
    legislators_repository = None
    politicians_repository = None

    @classmethod
    def setUpClass(cls):
        """Set up magic mocks as db in repositories before running tests"""
        cls.committees_repository = CommitteesRepository(MagicMock())
        cls.sessions_repository = SessionsRepository(MagicMock())
        cls.legislators_repository = LegislatorsRepository(MagicMock())
        cls.politicians_repository = PoliticiansRepository(MagicMock())

    def tearDown(self):
        self.committees_repository.db.reset_mock()
        self.sessions_repository.db.reset_mock()
        self.legislators_repository.db.reset_mock()
        self.politicians_repository.db.reset_mock()

    def test_get_by_id(self):
        """Test getting by ID"""
        test_id = 1
        self.committees_repository.get_by_id(test_id)
        self.sessions_repository.get_by_id(test_id)
        self.legislators_repository.get_by_id(test_id)
        self.politicians_repository.get_by_id(test_id)

        self.committees_repository.db.get_or_404.assert_called_once_with(Committee, test_id)

        self.legislators_repository.db.get_or_404.assert_called_once_with(Legislator, test_id)

        self.sessions_repository.db.get_or_404.assert_called_once_with(Session, test_id)

        self.politicians_repository.db.get_or_404.assert_called_once_with(Politician, test_id)

    def test_get_all_no_dict(self):
        """Test getting all"""
        self.committees_repository.get_all()
        self.sessions_repository.get_all()
        self.legislators_repository.get_all()
        self.politicians_repository.get_all()

        self.committees_repository.db.session.execute.assert_called_once()
        self.committees_repository.db.select.assert_called_once_with(Committee)

        self.legislators_repository.db.session.execute.assert_called_once()
        self.legislators_repository.db.select.assert_called_once_with(Legislator)

        self.sessions_repository.db.session.execute.assert_called_once()
        self.sessions_repository.db.select.assert_called_once_with(Session)

        self.politicians_repository.db.session.execute.assert_called_once()
        self.politicians_repository.db.select.assert_called_once_with(Politician)

    def test_get_all_by_state(self):
        """Test getting all"""
        filter = {
            "state": "ca"
        }
        self.sessions_repository.get_all(filter)
        self.legislators_repository.get_all(filter)
        self.politicians_repository.get_all(filter)

        self.legislators_repository.db.session.execute.assert_called_once()
        self.legislators_repository.db.select.assert_called_once_with(Legislator)

        self.sessions_repository.db.session.execute.assert_called_once()
        self.sessions_repository.db.select.assert_called_once_with(Session)

        self.politicians_repository.db.session.execute.assert_called_once()
        self.politicians_repository.db.select.assert_called_once_with(Politician)

    def test_politicians_get_all_filters(self):
        """Test getting Politician using filters"""
        filters = {
            'name': 'name',
            'state': 'or',
        }
        self.politicians_repository.get_all(filters)

        self.politicians_repository.db.session.execute.assert_called_once()
        self.politicians_repository.db.select.assert_called_once_with(Politician)
        # TODO assert search_string used somewhere in call
