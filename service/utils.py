"""Utils functions for app"""

import os
import json

from datetime import datetime, date, time

from .errors import NoSeedDataError
from .models import Legislator, Politician, Session, Committee


def preprocess():
    """Loads downloaded JSON data from OLIS 
       Returns data compatible with the service models"""
    legislators = []
    committees = []
    sessions = []
    politicians = {} # Maps legislator full name to Politician model

    data_path = os.getcwd()+os.getenv('DATA_PATH', '/data')
    try:
        # Open all files data dir
        for filename in os.listdir(data_path):
            filepath = os.path.join(data_path, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                _to_seed_data(data, legislators, sessions, committees, politicians)
    except FileNotFoundError:
        raise NoSeedDataError("Error: File not found at ", data_path)
    except json.JSONDecodeError:
        raise NoSeedDataError("Error: Could not decide JSON in ", data_path)
    return politicians.values(), sessions, legislators, committees

def _to_seed_data(data: dict, all_legislators: list, all_sessions: list, all_committees: list, pols: set):
    """Tranforms scraped data into one compatible with service data model"""
    # Add to seed_data
    for sess in data:
        if "SessionName" in sess:
            format_string = "%Y-%m-%dT%H:%M:%S"

            # Parse through data from OLIS
            session = Session(
                name=sess["SessionName"],
                begin_date=datetime.strptime(sess["BeginDate"], format_string),
                end_date=datetime.strptime(sess["EndDate"] or sess["ModifiedDate"], format_string)
            )
            all_sessions.append(session)

            # Add legislators from this session
            for leg in sess['Legislators']:
                pols_key = leg['FirstName']+" "+leg['LastName']
                if pols_key not in pols:
                    pol = Politician(first_name=leg["FirstName"], last_name=leg["LastName"])
                    pols[pols_key] = pol
                politician = pols[pols_key]

                l = Legislator(
                        title=leg["Title"],
                        leg_code = leg["LegislatorCode"],
                        district_number = leg["DistrictNumber"],
                        party = leg["Party"],
                        begin_date = datetime.strptime(leg["CreatedDate"], format_string),
                        # TODO: fix; there are serveral nulls in leg["ModifiedDate"]
                        end_date = datetime.now(),
                        session=session,
                        politician=politician,
                        state="OR",
                    )
                all_legislators.append(l)

            # Add committees from this session
            for com in sess['Committees']:
                comm = Committee(
                        name=com['CommitteeName'],
                        committee_type=com['CommitteeType'],
                        session=session
                    )
                all_committees.append(comm)
        else:
            # Parse scraped data
            format_string = "%Y-%m-%d"
            begin_date = datetime.strptime(sess["begin_date"], format_string)
            end_date = datetime.strptime(sess["end_date"], format_string)
            time_of_date = time(0, 0, 0)

            session = Session(
                name=sess["name"],
                begin_date=datetime.combine(begin_date, time_of_date),
                end_date=datetime.combine(end_date, time_of_date),
            )
            all_sessions.append(session)

            for legislator in sess["legislators"]:
                pols_key = legislator['first_name']+" "+legislator['last_name']
                if pols_key not in pols:
                    pols[pols_key] = Politician(first_name=legislator["first_name"], last_name=legislator["last_name"])
                politician = pols[pols_key]

                all_legislators.append(Legislator(
                    title=legislator["title"],
                    district_number=legislator["district_number"],
                    state=legislator["state"],
                    party=legislator["party"],
                    begin_date=session.begin_date,
                    end_date=session.end_date,
                    leg_code=f'{legislator["title"]} {legislator["last_name"]}',
                    politician=politician,
                    session=session,
                ))

            for committee in sess["committees"]:
                all_committees.append(Committee(
                        name=committee["name"],
                        committee_type=committee["committee_type"],
                        session = session
                ))
