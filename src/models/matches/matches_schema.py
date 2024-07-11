from marshmallow import Schema, fields


class MatchResponse(Schema):
    id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    result = fields.Str(required=True)
    player_name_1 = fields.Str(required=True)
    player_name_2 = fields.Str(required=True)
    player_name_3 = fields.Str(required=True)
    player_name_4 = fields.Str(required=True)
    date = fields.Date(required=True)
    place = fields.Integer(required=True)


class MatchesListSchema(Schema):
    items = fields.List(fields.Nested(MatchResponse))
    total = fields.Int(required=True)
    