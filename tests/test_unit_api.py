'''
Unit tests for the OlisAPI wrapper
'''


import unittest, json

from unittest.mock import MagicMock, patch

from wrapper import OlisAPI, utils

from tests import constants as test_constants


class TestOlisAPIUnit(unittest.TestCase):
    """
    Unit tests for OlisAPI wrapper
    """
    api = None

    def setUp(self):
        self.api = OlisAPI()
        self.api.session = MagicMock()


    def test_get_current_session(self):
        """Test code for getting current session"""
        # Set up mocked return value
        self.api.session.get.return_value = MockSessionValue({
                "odata.metadata": "endpoint_for_olisAPI/$metadata#EntityName",
                "value": ""
            })

        mocked_response = self.api.get_current_session()
        self.assertIsNotNone(mocked_response)
        self.api.session.get.assert_called_once()
        self.api.session.get.assert_called_with(test_constants.GET_CURRENT_SESSION_ENDPOINT+'&$format=json')

    def test_get_legislator(self):
        """Test code for getting legislator"""
        # Set up mocked return value
        self.api.session.get.return_value = MockSessionValue({
            "odata.metadata": "endpoint_for_olisAPI/$metadata#EntityName/@Element",
            "SessionKey": test_constants.UNIT_SESSION_KEY,
            "LegislatorCode": "Sen Senn",
            "FirstName": "F",
            "LastName": "Senn",
            "CapitolAddress": "900 Court St NE, Salem, OR, 97301",
            "CapitolPhone": "503-503-5033",
            "Title": "Senator",
            "Chamber": "S",
            "Party": "",
            "DistrictNumber": "0",
            "EmailAddress": "leg_email@domain.gov",
            "WebSiteUrl": "olis_url.gov/leg_website",
            "CreatedDate": "2022-11-22T14:14:14",
            "ModifiedDate": "2025-01-15T12:12:12"
        })

        mocked_response = self.api.get_legislator(test_constants.UNIT_SESSION_KEY, test_constants.UNIT_LEG_CODE)
        self.assertIsNotNone(mocked_response)
        self.api.session.get.assert_called_once()
        self.api.session.get.assert_called_with(
            test_constants.GET_LEGISLATOR_ENDPOINT.format(test_constants.UNIT_SESSION_KEY, 
                                                          test_constants.UNIT_LEG_CODE)+'?$format=json')


class MockSessionValue:
    value = {}

    def __init__(self, value: dict):
        self.value = value
    
    def json(self):
        return json.dumps(self.value)

if __name__ == '__main__':
    unittest.main()