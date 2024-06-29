from marshmallow import Schema, fields


class LeagueInputSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    created_by = fields.Integer(required=True)
    enrolments = fields.Integer(required=True)
    points_victory = fields.Int(required=True)
    points_defeat = fields.Int(required=True)
    weeks = fields.Int(required=True)
    weeks_played = fields.Int(required=True)
    date_start = fields.Date(required=True)


class LeagueListSchema(Schema):
    items = fields.List(fields.Nested(LeagueInputSchema))
    total = fields.Int(required=True)


class CreateLeagueSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    created_by = fields.Integer(required=True)
    points_victory = fields.Int(required=True)
    points_defeat = fields.Int(required=True)
    weeks = fields.Int(required=True)
    date_start = fields.Date(required=True)


class ModifyLeagueInputSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    points_victory = fields.Int(required=True)
    points_defeat = fields.Int(required=True)
    weeks = fields.Int(required=True)
    date_start = fields.Date(required=True)
