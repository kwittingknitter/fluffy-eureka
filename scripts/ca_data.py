"""Scrape and organize CA state data to resemble data file scraped from OLIS"""
import json
import os
import sys

from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from scrapers import ca_assembly_scraper, ca_senate_scraper

# TODO get past session info

# Get info about ca leg
assembly_members = ca_assembly_scraper.get_members()

senators = ca_senate_scraper.get_senators()
committees = ca_senate_scraper.get_committees()

# Save as JSON
format_string = "%Y-%m-%d"

current_session = {
    "name": "2025-2026 Regular Session",
    "begin_date": datetime.strptime("2025-01-06", format_string),
    "end_date": datetime.strptime("2026-12-04", format_string),
    "committees": committees,
    "legislators": senators + assembly_members,
}

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    return ''

with open('./../data/ca_current_session.json', 'w') as f:
    f.write(json.dumps(
    [current_session],
    indent=4,
    separators=(',', ': '),
    default=set_default
    ))