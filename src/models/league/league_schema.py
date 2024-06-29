from marshmallow import Schema, fields


class LeagueInputSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    created_by = fields.Integer(required=True)
    enrolments = fields.Integer(required=True)
    points_victory = fields.Int()
    points_defeat = fields.Int()
    weeks = fields.Int()
    weeks_played = fields.Int()
    date_start = fields.Date()


class LeagueListSchema(Schema):
    items = fields.List(fields.Nested(LeagueInputSchema))
    total = fields.Int(required=True)


class CreateLeagueSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    created_by = fields.Integer(required=True)
    points_victory = fields.Int()
    points_defeat = fields.Int()
    weeks = fields.Int()
    weeks_played = fields.Int()
    date_start = fields.Date()


class ModifyLeagueInputSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
