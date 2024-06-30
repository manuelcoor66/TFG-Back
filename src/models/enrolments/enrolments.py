from typing import Any

from src.models import db
from src.models.enrolments.enrolments_exceptions import (
    EnrolmentIdException,
    EnrolmentUserIdException,
    EnrolmentLeagueIdException,
    EnrolmentsException,
    EnrolmentException,
)
from src.models.league import League
from src.models.league.league_exceptions import LeagueIdException


class Enrolment(db.Model):
    __tablename__ = "enrolments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    league_id = db.Column(db.Integer, db.ForeignKey("league.id"))
    points = db.Column(db.Integer)
    matches_played = db.Column(db.Integer)
    paid = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    finalized = db.Column(db.Boolean)

    def __init__(
        self, user_id, league_id, points, matches_played, paid, active, finalized
    ):
        self.user_id = user_id
        self.league_id = league_id
        self.points = points
        self.matches_played = matches_played
        self.paid = paid
        self.active = active
        self.finalized = finalized

    def __repr__(self):
        return f"<Enrolment(id={self.id}, user_id={self.user_id}, league_id={self.league_id}"

    @classmethod
    def get_enrolment_by_id(cls, id: int) -> "Enrolment":
        """
        Return an existing enrolment
        :param id:
        :return:
        """
        enrolment = db.session.query(Enrolment).filter_by(id=id).first()

        if enrolment:
            return enrolment
        else:
            raise EnrolmentIdException

    @classmethod
    def get_enrolments_by_user_id(cls, user_id: int) -> list[dict[str, Any]]:
        """
        Return an existing enrolment
        :param user_id:
        :return:
        """
        enrolments = db.session.query(Enrolment).filter_by(user_id=user_id).all()

        if enrolments:
            serialized_enrolments = []
            for enrolment in enrolments:
                serialized_enrolment = {
                    "id": enrolment.id,
                    "user_id": enrolment.user_id,
                    "league_id": enrolment.league_id,
                    "points": enrolment.points,
                    "matches_played": enrolment.matches_played,
                    "paid": enrolment.paid,
                    "active": enrolment.active,
                    "finalized": enrolment.finalized,
                }

                serialized_enrolments.append(serialized_enrolment)

            return serialized_enrolments
        else:
            raise EnrolmentUserIdException

    @classmethod
    def get_enrolments_by_league_id(cls, league_id: int) -> list[dict[str, Any]]:
        """
        Return an existing enrolment
        :param league_id:
        :return:
        """
        enrolments = db.session.query(Enrolment).filter_by(league_id=league_id).all()

        if enrolments:
            serialized_enrolments = []
            for enrolment in enrolments:
                serialized_enrolment = {
                    "id": enrolment.id,
                    "user_id": enrolment.user_id,
                    "league_id": enrolment.league_id,
                    "points": enrolment.points,
                    "matches_played": enrolment.matches_played,
                    "paid": enrolment.paid,
                    "active": enrolment.active,
                    "finalized": enrolment.finalized,
                }

                serialized_enrolments.append(serialized_enrolment)

            return serialized_enrolments
        else:
            raise EnrolmentLeagueIdException

    @classmethod
    def get_all_enrolments(cls) -> list[dict[str, Any]]:
        enrolments = db.session.query(Enrolment).all()

        if enrolments:
            serialized_enrolments = []
            for enrolment in enrolments:
                serialized_enrolment = {
                    "id": enrolment.id,
                    "user_id": enrolment.user_id,
                    "league_id": enrolment.league_id,
                    "points": enrolment.points,
                    "matches_played": enrolment.matches_played,
                    "paid": enrolment.paid,
                    "active": enrolment.active,
                    "finalized": enrolment.finalized,
                }

                serialized_enrolments.append(serialized_enrolment)

            return serialized_enrolments
        else:
            raise EnrolmentsException

    @classmethod
    def add_new_enrolment(cls, user_id: int, league_id: int, paid: bool):
        new_enrolment = Enrolment(
            user_id=user_id,
            league_id=league_id,
            points=0,
            matches_played=0,
            paid=paid,
            active=True,
            finalized=False,
        )

        try:
            db.session.add(new_enrolment)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @classmethod
    def add_new_match(cls, user_id: int, league_id: int, win: bool):
        enrolment = (
            db.session.query(Enrolment)
            .filter_by(league_id=league_id, user_id=user_id)
            .first()
        )

        if enrolment:
            league = db.session.query(League).filter_by(id=league_id).first()

            if league:
                enrolment.matches_played += 1
                print(enrolment.matches_played)
                if win is True:
                    enrolment.points += league.points_victory
                else:
                    enrolment.points += league.points_defeat
                try:
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    raise e
            else:
                raise LeagueIdException
        else:
            raise EnrolmentException
