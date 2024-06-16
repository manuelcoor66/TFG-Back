from marshmallow import Schema, fields


class CreateUserInputSchema(Schema):
    name = fields.Str(required=True)
    last_names = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    security_word = fields.Str(required=True)


class UserInputSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    last_names = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    security_word = fields.Str(required=True)


class ModifyUserInputSchema(Schema):
    name = fields.Str(required=False)
    last_names = fields.Str(required=False)
    email = fields.Email(required=True)
    password = fields.Str(required=False)
    security_word = fields.Str(required=False)


class UserListSchema(Schema):
    items = fields.List(fields.Nested(UserInputSchema))
    total = fields.Int(required=True)


class UserInputPasswordSchema(Schema):
    email = fields.Email(required=True)
    new_password = fields.Str(required=True)


class UserInputSecurityWordSchema(Schema):
    email = fields.Email(required=True)
    security_word = fields.Str(required=True)


class UserInputMatchSchema(Schema):
    email = fields.Email(required=True)


class UserMatchesSchema(Schema):
    matches = fields.Integer(required=True)


class UserWinsSchema(Schema):
    matches = fields.Integer(required=True)
    wins = fields.Integer(required=True)