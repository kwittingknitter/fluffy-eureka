'''
Wrapper for OLIS API
'''


from requests import Session, Response

from wrapper import utils


class OlisAPI:
    """Wrapper for OLIS API"""

    def __init__(self):
        self.session = Session()

    def _json_format(self, endpoint):
        if '?' in endpoint:
            return endpoint + '&$format=json'
        return endpoint + '?$format=json'

    def get_current_session(self) -> Response:
        endpoint = self._json_format(
            utils.get_endpoint(utils.Operation.GET_CURRENT_SESSION))
        return self.session.get(endpoint).json()

    def get_legislator(self, session_key: str, legislator_code: str) -> Response:
        endpoint = self._json_format(
            utils.get_endpoint(utils.Operation.GET_LEG).format(
            session_key, legislator_code))
        return self.session.get(endpoint).json()

    def get_legislator_chief_sponsored_bills(
            self,
            session_key: str,
            legislator_key: str
        ) -> Response:
        endpoint = self._json_format(
            utils.get_endpoint(utils.Operation.GET_LEG_CHIEF_BILLS).format(
                session_key, legislator_key))
        return self.session.get(endpoint).json()

    def get_legislator_sponsored_bills(
            self,
            session_key: str,
            legislator_key: str
        ) -> Response:
        endpoint = self._json_format(
            utils.get_endpoint(utils.Operation.GET_LEG_BILLS).format(session_key, legislator_key))
        return self.session.get(endpoint).json()

    def get_legislator_sponsored_bills_enrolled(
            self,
            session_key: str,
            legislator_key: str
        ) -> Response:
        endpoint = self._json_format(
            utils.get_endpoint(
                utils.Operation.GET_LEG_BILLS_ENROLLED).format(session_key, legislator_key))
        return self.session.get(endpoint).json()
