from typing import Any

from sqlalchemy import Date, Enum, func

from src.models import db
from src.models.league import League
from src.models.ticket.ticket_exception import (
    TicketIdException,
    TicketsException,
    UserTicketsException,
)
from src.models.user import User
from src.utils.ticketEnum import TicketState


class Ticket(db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    state = db.Column(Enum(TicketState), nullable=False)
    date = db.Column(db.Date)

    def __init__(self, league_id: int, user_id: int, state: str, date: Date):
        self.league_id = league_id
        self.user_id = user_id
        self.state = state
        self.date = date

    def __repr__(self):
        return f"<Ticket(id={self.id}, state={self.state}, date={self.date})>"

    @classmethod
    def get_by_id(cls, id: int) -> "Ticket":
        """
        Returns an existing ticket
        :return:
        """
        ticket = db.session.query(Ticket).filter_by(id=id).first()

        if ticket:
            return ticket
        else:
            raise TicketIdException

    @classmethod
    def get_all_tickets(cls) -> list[dict[str, Any]]:
        """
        Returns a list of all tickets
        :return:
        """
        tickets = db.session.query(Ticket).all()

        if tickets:
            serialized_tickets = []
            for ticket in tickets:
                user_name = User.get_user_name(ticket.user_id)
                league = League.get_league_by_id(ticket.league_id)

                serialized_ticket = {
                    "id": ticket.id,
                    "league_name": league.name,
                    "user_name": user_name,
                    "state": ticket.state,
                    "date": ticket.date,
                }

                serialized_tickets.append(serialized_ticket)

            return serialized_tickets
        else:
            raise TicketsException

    @classmethod
    def add_new_ticket(
        cls, league_id: int, user_id: int, state: TicketState, date: Date
    ) -> "Ticket":
        """
        Creates a new ticket
        :param league_id:
        :param user_id:
        :param state:
        :param date:
        :return:
        """
        new_ticket = Ticket(
            league_id=league_id, user_id=user_id, state=state.name, date=date
        )
        try:
            db.session.add(new_ticket)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return new_ticket

    @classmethod
    def get_user_tickets(cls, user_id: int) -> list[dict[str, Any]]:
        """
        Gets the most recent ticket for each league for a user
        :param user_id:
        :return:
        """
        subquery = (
            db.session.query(
                Ticket.user_id,
                Ticket.league_id,
                func.max(Ticket.date).label("max_date"),
            )
            .filter_by(user_id=user_id)
            .group_by(Ticket.user_id, Ticket.league_id)
            .subquery()
        )

        tickets = (
            db.session.query(Ticket)
            .join(
                subquery,
                (Ticket.user_id == subquery.c.user_id)
                & (Ticket.league_id == subquery.c.league_id)
                & (Ticket.date == subquery.c.max_date),
            )
            .all()
        )

        user = User.get_user_by_id(user_id)
        if tickets:
            serialized_tickets = []
            for ticket in tickets:
                print(ticket)
                league = league = db.session.query(League).filter_by(id=ticket.league_id).first()

                serialized_ticket = {
                    "id": league.id,
                    "league_name": league.name,
                    "user_name": user.name + " " + user.last_names,
                    "state": ticket.state,
                    "date": ticket.date,
                }

                serialized_tickets.append(serialized_ticket)

            return serialized_tickets
        else:
            raise UserTicketsException
