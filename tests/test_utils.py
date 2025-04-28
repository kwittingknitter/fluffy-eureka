'''
Unit tests for wrapper.utils
'''

import unittest

from wrapper.utils import *

from tests.constants import *


class TestGetEndpoint(unittest.TestCase):
    '''
    Tests for wrapper.utils.get_endpoint tested against constants in tests.constants
    '''
    def test_current_session_endpoint(self):
        self.assertEqual(get_endpoint(Operation.GET_CURRENT_SESSION), GET_CURRENT_SESSION_ENDPOINT)

    def test_get_legislator(self):
        self.assertEqual(get_endpoint(Operation.GET_LEG), GET_LEGISLATOR_ENDPOINT)
    
    def test_get_legislator_bills(self):
        self.assertEqual(get_endpoint(Operation.GET_LEG_BILLS), 
                         GET_LEGISLATOR_BILLS)
    
    def test_get_legislator_chief_bills(self):
        self.assertEqual(get_endpoint(Operation.GET_LEG_CHIEF_BILLS), 
                         GET_LEGISLATOR_CHIEF_BILLS)
    
    def test_get_legislator_bills_enrolled(self):
        self.assertEqual(get_endpoint(Operation.GET_LEG_BILLS_ENROLLED), 
                         GET_LEGISLATOR_BILLS_ENROLLED)

    def test_get_bad_operation(self):
        with self.assertRaises(TypeError):
            get_endpoint()


if __name__ == '__main__':
    unittest.main()