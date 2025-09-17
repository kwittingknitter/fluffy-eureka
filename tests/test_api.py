'''
Tests for the OlisAPI wrapper
'''


import unittest

from wrapper import OlisAPI


class TestOlisAPI(unittest.TestCase):
    '''
    Test suite for OlisAPI wrapper
    '''
    SESSION_KEY = '2023R1'
    LEG_CODE = 'Sen Lieber'
    api = OlisAPI()

    def test_get_current_session(self):
        """Test getting current session from OLIS"""
        response = self.api.get_current_session()
        self.assertIsNotNone(response)
        self.assertIn('odata.metadata', response)
        self.assertEqual(1, len(response['value']))
        response = response['value']
        self.assertIsNotNone(response[0])
        # Check for expands, keys
        keys_to_check = ['Committees', 'Legislators', 'SessionKey', 'SessionName']
        for key in keys_to_check:
            self.assertIn(key, response[0])

    def test_get_legislator(self):
        """Test for getting legislator from OLIS"""
        response = self.api.get_legislator(self.SESSION_KEY, self.LEG_CODE)
        self.assertIsNotNone(response)
        self.assertIn('odata.metadata', response)



if __name__ == '__main__':
    unittest.main()
