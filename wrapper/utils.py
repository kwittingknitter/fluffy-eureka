'''
Utils for wrapper
'''


from enum import Enum

from wrapper.constants import *


class Operation(Enum):
    GET_LEG = 0
    GET_CURRENT_SESSION = 1
    GET_LEG_BILLS = 2
    GET_LEG_CHIEF_BILLS = 3
    GET_LEG_BILLS_ENROLLED = 4
    GET_SESSIONS = 5
    GET_SESSION_BILLS = 5

def get_endpoint(operation: str) -> str:
    '''
    Returns endpoint based on operation
    '''
    match operation:
        case Operation.GET_CURRENT_SESSION:
            return BASE_URL+"{}?$filter={} &$expand={}".format(
                ENDPOINT['session'], FILTERS['current_session'],
                EXPAND['session'])
        case Operation.GET_SESSION_BILLS:
            return BASE_URL+ENDPOINT['session']+"(SessionKey='{}')/?$expand="+EXPAND['session_bills']
        case Operation.GET_SESSIONS:
            return BASE_URL+"{}?$expand={}".format(
                ENDPOINT['session'], EXPAND['session'])
        case Operation.GET_LEG:
            return BASE_URL+"{}".format(
                ENDPOINT['legislators'])+"(SessionKey='{}', LegislatorCode='{}')"
        case Operation.GET_LEG_BILLS:
            return BASE_URL+"{}?$filter={} &$expand={}".format(
                ENDPOINT['sponsor'], FILTERS['bills_sponsored'], EXPAND['bills']
            )
        case Operation.GET_LEG_CHIEF_BILLS:
            return BASE_URL+"{}?$filter={} and {} &$expand={}".format(
                ENDPOINT['sponsor'], FILTERS['bills_sponsored'],
                FILTERS['chief_sponsor'], EXPAND['bills']
            )
        case Operation.GET_LEG_BILLS_ENROLLED:
            return BASE_URL+"{}?$filter={} and {} &$expand={}".format(
                ENDPOINT['sponsor'], FILTERS['bills_sponsored'],
                FILTERS['enrolled_bills'], EXPAND['bills']
            )
        case any:
            raise Exception
