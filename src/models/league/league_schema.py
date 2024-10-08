from marshmallow import Schema, fields


class LeagueResponse(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    created_by = fields.Str(required=True)
    created_by_id = fields.Integer(required=True)
    enrolments = fields.Integer(required=True)
    points_victory = fields.Int(required=True)
    points_defeat = fields.Int(required=True)
    place = fields.Str(required=True)
    weeks = fields.Int(required=True)
    weeks_played = fields.Int(required=True)
    date_start = fields.DateTime(required=True)
    sport = fields.String(required=True)
    sport_icon = fields.String(required=True)
    price = fields.Int(required=True)


class LeagueListSchema(Schema):
    items = fields.List(fields.Nested(LeagueResponse))
    total = fields.Int(required=True)


class CreateLeagueSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    created_by = fields.Integer(required=True)
    points_victory = fields.Int(required=True)
    place = fields.Int(required=True)
    points_defeat = fields.Int(required=True)
    weeks = fields.Int(required=True)
    date_start = fields.DateTime(required=True)
    sport_id = fields.Integer(required=True)
    price = fields.Int(required=True)


class ModifyLeagueResponse(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    points_victory = fields.Int(required=True)
    points_defeat = fields.Int(required=True)
    weeks = fields.Int(required=True)
    date_start = fields.DateTime(required=True)


class LeagueIdSchema(Schema):
    id = fields.Integer(required=True)


class LeagueSearchSchema(Schema):
    search = fields.Str(required=False)
