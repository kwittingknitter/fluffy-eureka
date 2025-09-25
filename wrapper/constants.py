"""
Constants for wrapper
"""


BASE_URL = 'https://api.oregonlegislature.gov/odata/odataservice.svc/'
ENDPOINT = {
    'legislators': 'Legislators',
    'session': 'LegislativeSessions',
    'sponsor': 'MeasureSponsors',
}
FILTERS = {
    'current_session': "DefaultSession eq true",
    'bills_sponsored': "SessionKey eq '{}' and LegislatoreCode eq '{}'",
    # MeasureSponsor data model says "LegislatoreCode"
    # https://www.oregonlegislature.gov/citizen_engagement/Documents/OLOData-Model.pdf
    'chief_sponsor': "SponsorLevel eq 'Chief'",
    'enrolled_bills': "Measure/CurrentLocation eq 'Chapter Number Assigned'" 
}
EXPAND = {
    'session': 'Legislators, Committees',
    'session_bills': 'Measures',
    'bills': 'Measure'
}
