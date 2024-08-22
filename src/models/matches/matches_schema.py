from marshmallow import Schema, fields


class MatchResponse(Schema):
    id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    result = fields.Str(required=True)
    player_name_1 = fields.Str(required=True)
    player_name_2 = fields.Str(required=False)
    player_name_3 = fields.Str(required=False)
    player_name_4 = fields.Str(required=False)
    date = fields.DateTime(required=True)
    place = fields.Integer(required=True)


class MatchesListSchema(Schema):
    items = fields.List(fields.Nested(MatchResponse))
    total = fields.Int(required=True)


class CreateMatchSchema(Schema):
    league_id = fields.Integer(required=True)
    player_name_1 = fields.Integer(required=False)
    date = fields.DateTime(required=True)
    place = fields.Integer(required=True)


class AddNewPlayerSchema(Schema):
    match_id = fields.Integer(required=True)
    player_id = fields.Integer(required=False)


class AddResultSchema(Schema):
    match_id = fields.Integer(required=True)
    result = fields.Str(required=False)
    win_player_1 = fields.Str(required=True)
    win_player_2 = fields.Str(required=True)
    win_player_3 = fields.Str(required=False)
    win_player_4 = fields.Str(required=False)


class MatchAddResponse(Schema):
    id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    result = fields.Str(required=True)
    player_id_1 = fields.Str(required=False)
    player_id_2 = fields.Str(required=False)
    player_id_3 = fields.Str(required=False)
    player_id_4 = fields.Str(required=False)
    date = fields.DateTime(required=True)
    place = fields.Integer(required=True)
