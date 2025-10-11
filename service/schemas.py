"""Model schemas for JSON ouptut in routes"""

from marshmallow import Schema, fields


class LegislatorScheme(Schema):
    """Output schema for Legislator model"""
    id = fields.Integer()
    title = fields.String()
    leg_code = fields.String()
    district_number = fields.Integer()
    party = fields.String()
    begin_date = fields.Date()
    end_date = fields.Date(allow_none=True)
    session_id = fields.Integer()
    politician_id = fields.Integer()


class CommitteeScheme(Schema):
    """Output schema for Committee model"""
    id = fields.Integer()
    name = fields.String()
    committee_type = fields.String()
    session_id = fields.Integer()


class PoliticianScheme(Schema):
    """Output schema for Politician model"""
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    legislators = fields.Nested(
        LegislatorScheme, only=('id', 'leg_code', 'title', 'begin_date'), many=True)

class SessionScheme(Schema):
    """Output schema for Session model"""
    id = fields.Integer()
    name = fields.String()
    begin_date = fields.Date()
    end_date = fields.Date(allow_none=True)
    committees = fields.Nested(CommitteeScheme, only=('id', 'name'), many=True)
    legislators = fields.Nested(LegislatorScheme, only=('id', 'leg_code'), many=True)
