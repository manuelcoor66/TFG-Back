from marshmallow import Schema, fields

from src.utils.ticketEnum import TicketState


class TicketInputScheme(Schema):
    id = fields.Integer(required=True)
    league_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    state = fields.Enum(TicketState, required=True)
    date = fields.DateTime(required=True)


class CreateTicketScheme(Schema):
    league_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    state = fields.Enum(TicketState, required=True)
    date = fields.DateTime(required=True)


class TicketUserScheme(Schema):
    id = fields.Integer(required=True)
    league_name = fields.String(required=True)
    user_name = fields.String(required=True)
    state = fields.Enum(TicketState, required=True)
    date = fields.DateTime(required=True)


class TicketUserListSchema(Schema):
    items = fields.List(fields.Nested(TicketUserScheme))
    total = fields.Int(required=True)
