'''
Unit tests for the OlisAPI wrapper
'''


import requests, unittest

from unittest.mock import MagicMock, patch

from wrapper import OlisAPI, utils

from tests import constants as test_constants


class TestOlisAPIUnit(unittest.TestCase):

    @patch('requests.Session')
    def test_get_current_session(self, mock):
        """Test code for getting current session"""
        mock.return_value.get.return_value = {
            "odata.metadata": "endpoint_for_olisAPI/$metadata#EntityName",
            "value": ""
        }

        def get_endpoint(op: utils.Operation):
            return test_constants.UNIT_CURRENT_SESSION_ENDPOINT

        with patch('wrapper.utils.get_endpoint', get_endpoint):
            api = OlisAPI()
            api.session = mock
            mocked_response = api.get_current_session()
            mock.assert_called_with('get', test_constants.UNIT_CURRENT_SESSION_ENDPOINT)

    @patch('requests.Session')
    def test_get_legislator(self, mock):
        """Test code for getting legislator"""
        mock.return_value.get.return_value = {
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
        }

        def get_endpoint(op: utils.Operation):
            return test_constants.UNIT_GET_LEGISLATOR_ENDPOINT

        with patch('wrapper.utils.get_endpoint', get_endpoint):
            api = OlisAPI()
            api.session = mock
            mocked_response = api.get_legislator(test_constants.UNIT_SESSION_KEY, test_constants.UNIT_LEG_CODE)
            mocked_response.assert_called_with('get', test_constants.UNIT_GET_LEGISLATOR_ENDPOINT)


if __name__ == '__main__':
    unittest.main()