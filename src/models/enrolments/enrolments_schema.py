from marshmallow import Schema, fields


class EnrolmentInputSchema(Schema):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    points = fields.Float(required=True)
    matches_played = fields.Integer(required=True)
    paid = fields.Boolean(required=True)
    active = fields.Boolean(required=True)
    finalized = fields.Boolean(required=True)


class EnrolmentListSchema(Schema):
    items = fields.List(fields.Nested(EnrolmentInputSchema))
    total = fields.Int(required=True)


class CreateEnrolmentSchema(Schema):
    user_id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    paid = fields.Boolean(required=True)


class AddMatchSchema(Schema):
    user_id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    win = fields.Boolean(required=True)


class EnrolmentSchema(Schema):
    user_id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
