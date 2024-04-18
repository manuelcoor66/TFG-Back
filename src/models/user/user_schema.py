from marshmallow import Schema, fields


class UserInputSchema(Schema):
    name = fields.Str(required=True)
    last_names = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    security_word = fields.Str(required=True)


class UserListSchema(Schema):
    items = fields.List(fields.Nested(UserInputSchema))
    total = fields.Int(required=True)

class UserInputPasswordSchema(Schema):
    email = fields.Email(required=True)
    new_password = fields.Str(required=True)
