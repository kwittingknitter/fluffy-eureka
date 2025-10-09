'''Scripts for Flask app'''

import os
import json

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, inspect

from errors import NoSeedDataError
from models import Legislator, Politician, Session, Committee


def insert_seed_data(db: SQLAlchemy):
    """Inserts seed data into the database, db"""
    inspector = inspect(db.engine)
    if inspector.get_table_names():
        pass

    politicians, sessions, legislators, committees = preprocess()
    db.session.add_all(politicians)
    db.session.add_all(sessions)
    db.session.add_all(legislators)
    db.session.add_all(committees)
    db.session.commit()

def preprocess():
    """Loads downloaded JSON data from OLIS 
       Returns data compatible with the models in ../models.py"""
    data_path = os.getcwd()+os.getenv('DATA_PATH', '/sessions.json')
    try:
        with open(data_path, 'r') as file:
            data = json.load(file)
            return _to_seed_data(data)
    except FileNotFoundError:
        raise NoSeedDataError("Error: File not found at ", data_path)
    except json.JSONDecodeError:
        raise NoSeedDataError("Error: Could not decide JSON in ", data_path)

def _to_seed_data(data: dict):
    """Tranforms data from OLIS API into one compatible with our data model
        OLIS API downloaded sessions data contains:
            Committees, Legislators, SessionKey, SessionName, BeginDate, 
            EndDate, CreatedDate, ModifiedDate, DefaultSession
    """
    # 2014-12-18T18:52:36
    format_string = "%Y-%m-%dT%H:%M:%S"

    all_legislators = []
    all_committees = []
    all_sessions = []
    pols = {} # Maps legislator full name to Politician model

    # Add to seed_data
    for sess in data:
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

    return pols.values(), all_sessions, all_legislators, all_committees
