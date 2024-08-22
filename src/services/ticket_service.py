import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.ticket import (
    Ticket,
    TicketInputScheme,
    TicketUserListSchema,
    CreateTicketScheme,
)
from src.models.ticket.ticket_exception import (
    TicketsException,
    TicketIdException,
    UserTicketsException,
)

api_url = "/ticket"
api_name = "Ticket"
api_description = "Ticket service"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)


@blp.route("/<int:ticket_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, TicketInputScheme)
def get_ticket_by_id(ticket_id: int):
    """
    Get a ticket by his id
    """
    try:
        ticket = Ticket.get_by_id(ticket_id)

        return ticket
    except TicketIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/user/<int:user_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, TicketUserListSchema)
def get_user_tickets(user_id: int):
    """
    Get all the tickets of an user
    """
    try:
        tickets = Ticket.get_user_tickets(user_id)

        return {"items": tickets, "total": len(tickets)}
    except UserTicketsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/list", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, TicketUserListSchema)
def get_all_tickets():
    """
    Get all the tickets
    """
    try:
        tickets = Ticket.get_all_tickets()

        return {"items": tickets, "total": len(tickets)}
    except TicketsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/create", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(CreateTicketScheme, location="query")
@blp.response(200, TicketInputScheme)
def create_ticket(data):
    """
    Create a new ticket
    """
    try:
        new_ticket = Ticket.add_new_ticket(
            data.get("league_id"),
            data.get("user_id"),
            data.get("state"),
            data.get("date"),
        )

        return new_ticket
    except Exception as e:
        return {"message": str(e)}
