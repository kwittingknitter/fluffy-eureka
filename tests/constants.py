'''
Constants used in tests
'''

GET_CURRENT_SESSION_ENDPOINT = 'https://api.oregonlegislature.gov/odata/odataservice.svc/LegislativeSessions?$filter=DefaultSession eq true &$expand=Legislators, Committees'
GET_LEGISLATOR_ENDPOINT = "https://api.oregonlegislature.gov/odata/odataservice.svc/Legislators(SessionKey='{}', LegislatorCode='{}')"
GET_LEGISLATOR_BILLS_ENROLLED = "https://api.oregonlegislature.gov/odata/odataservice.svc/MeasureSponsors?$filter=SessionKey eq '{}' and LegislatoreCode eq '{}' and Measure/CurrentLocation eq 'Chapter Number Assigned' &$expand=Measure"
GET_LEGISLATOR_BILLS = "https://api.oregonlegislature.gov/odata/odataservice.svc/MeasureSponsors?$filter=SessionKey eq '{}' and LegislatoreCode eq '{}' &$expand=Measure"
GET_LEGISLATOR_CHIEF_BILLS = "https://api.oregonlegislature.gov/odata/odataservice.svc/MeasureSponsors?$filter=SessionKey eq '{}' and LegislatoreCode eq '{}' and SponsorLevel eq \'Chief\' &$expand=Measure"

UNIT_CURRENT_SESSION_ENDPOINT = 'get_current_session_endpoint?$format=json'
UNIT_GET_LEGISLATOR_ENDPOINT = 'get_leg?filter=DefaultSession eq true&$format=json'
UNIT_SESSION_KEY = 'test_session_key'
UNIT_LEG_CODE = 'test_leg_code'