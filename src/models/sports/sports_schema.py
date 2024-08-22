from marshmallow import Schema, fields


class SportsSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    icon = fields.String(required=True)
    players = fields.Int(required=True)


class SportsListSchema(Schema):
    items = fields.List(fields.Nested(SportsSchema))
    total = fields.Int(required=True)


class CreateSportSchema(Schema):
    name = fields.String(required=True)
    icon = fields.String(required=True)
    players = fields.Int(required=True)
