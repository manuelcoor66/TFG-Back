from marshmallow import Schema, fields


class AchievementsInputSchema(Schema):
    id = fields.Integer(required=True)
    description = fields.Str(required=True)
    table = fields.Str(required=True)
    column = fields.Str(required=True)
    amount = fields.Integer(required=True)


class AchievementsListSchema(Schema):
    items = fields.List(fields.Nested(AchievementsInputSchema))
    total = fields.Int(required=True)


class CreateAchievementSchema(Schema):
    description = fields.Str(required=True)
    table = fields.Str(required=True)
    column = fields.Str(required=True)
    amount = fields.Integer(required=True)
