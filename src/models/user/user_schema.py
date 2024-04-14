from marshmallow import Schema, fields


class UserInputSchema(Schema):
    name = fields.Str(required=True)
    last_names = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    security_word = fields.Str(required=True)