from marshmallow import Schema, fields


class PlaceReturnSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    coordinates = fields.String(required=True)


class PlaceReturnListSchema(Schema):
    items = fields.List(fields.Nested(PlaceReturnSchema))
    total = fields.Int(required=True)


class PlaceInputSchema(Schema):
    name = fields.String(required=True)
    coordinates = fields.String(required=True)


class PlaceInputModifySchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=False)
    coordinates = fields.String(required=False)
