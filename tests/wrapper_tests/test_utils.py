'''
Unit tests for wrapper.utils
'''

import unittest


from wrapper.utils import Operation, get_endpoint
from wrapper.errors import UnsupportedOperationError

from .constants import GET_CURRENT_SESSION_ENDPOINT, GET_LEGISLATOR_ENDPOINT, \
    GET_LEGISLATOR_BILLS, GET_LEGISLATOR_CHIEF_BILLS, GET_LEGISLATOR_BILLS_ENROLLED


class TestGetEndpoint(unittest.TestCase):
    '''
    Tests for wrapper.utils.get_endpoint tested against constants in tests.constants
    '''
    def test_current_session_endpoint(self):
        """Test utils.get_endpoint for current session"""
        self.assertEqual(get_endpoint(Operation.GET_CURRENT_SESSION), GET_CURRENT_SESSION_ENDPOINT)

    def test_get_legislator(self):
        """Test utils.get_endpoint for getting a legislator"""
        self.assertEqual(get_endpoint(Operation.GET_LEG), GET_LEGISLATOR_ENDPOINT)

    def test_get_legislator_bills(self):
        """Test utils.get_endpoint for getting a legislator's sponsored bills"""
        self.assertEqual(get_endpoint(Operation.GET_LEG_BILLS),
                         GET_LEGISLATOR_BILLS)

    def test_get_legislator_chief_bills(self):
        """Test utils.get_endpoint for getting a legislator's chief sponsored bills"""
        self.assertEqual(get_endpoint(Operation.GET_LEG_CHIEF_BILLS),
                         GET_LEGISLATOR_CHIEF_BILLS)

    def test_get_legislator_bills_enrolled(self):
        """Test utils.get_endpoint for getting a legislator's bills that got enacted"""
        self.assertEqual(get_endpoint(Operation.GET_LEG_BILLS_ENROLLED),
                         GET_LEGISLATOR_BILLS_ENROLLED)

    def test_get_bad_operation(self):
        """Test utils.get_endpoint for throws error for unsupported operation"""
        with self.assertRaises(UnsupportedOperationError):
            get_endpoint(7)


if __name__ == '__main__':
    unittest.main()
