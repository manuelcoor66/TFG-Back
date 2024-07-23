from typing import Any

from sqlalchemy import desc

from src.models import db
from src.models.enrolments.enrolments_exceptions import (
    EnrolmentIdException,
    EnrolmentLeagueIdException,
    EnrolmentsException,
    EnrolmentException,
)
from src.models.league import League
from src.models.league.league_exceptions import LeagueIdException

from src.models.user import User


class Enrolment(db.Model):
    __tablename__ = "enrolments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    league_id = db.Column(db.Integer, db.ForeignKey("league.id"))
    points = db.Column(db.Integer)
    matches_played = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    defeats = db.Column(db.Integer)
    paid = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    finalized = db.Column(db.Boolean)

    def __init__(
        self, user_id, league_id, points, matches_played, paid, active, finalized, wins, defeats
    ):
        self.user_id = user_id
        self.league_id = league_id
        self.points = points
        self.matches_played = matches_played
        self.paid = paid
        self.active = active
        self.finalized = finalized
        self.wins = wins
        self.defeats = defeats

    def __repr__(self):
        return f"<Enrolment(id={self.id}, user_id={self.user_id}, league_id={self.league_id})>"

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
        enrolments = db.session.query(Enrolment).filter_by(user_id=user_id).order_by(desc(Enrolment.points)).all()

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
                "wins": enrolment.wins,
                "defeats": enrolment.defeats
            }

            serialized_enrolments.append(serialized_enrolment)

        return serialized_enrolments

    @classmethod
    def get_enrolments_by_league_id(cls, league_id: int) -> list[dict[str, Any]]:
        """
        Return an existing enrolment
        :param league_id:
        :return:
        """
        enrolments = db.session.query(Enrolment).filter_by(league_id=league_id).order_by(desc(Enrolment.points)).all()

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
                    "wins": enrolment.wins,
                    "defeats": enrolment.defeats
                }

                serialized_enrolments.append(serialized_enrolment)

            return serialized_enrolments
        else:
            raise EnrolmentLeagueIdException

    @classmethod
    def get_all_enrolments(cls) -> list[dict[str, Any]]:
        enrolments = db.session.query(Enrolment).order_by(desc(Enrolment.points)).all()

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
                    "wins": enrolment.wins,
                    "defeats": enrolment.defeats
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
            wins=0,
            defeats=0,
        )

        try:
            db.session.add(new_enrolment)
            db.session.commit()
            return new_enrolment
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
                if win is True:
                    enrolment.points += league.points_victory
                    enrolment.wins += 1
                else:
                    enrolment.points += league.points_defeat
                    enrolment.defeats += 1
                try:
                    db.session.commit()
                    return cls.get_all_enrolments()
                except Exception as e:
                    db.session.rollback()
                    raise e
            else:
                raise LeagueIdException
        else:
            raise EnrolmentException

    @classmethod
    def finalize_enrolment(cls, user_id: int, league_id: int):
        enrolment = (
            db.session.query(Enrolment)
            .filter_by(league_id=league_id, user_id=user_id)
            .first()
        )

        if enrolment:
            enrolment.finalized = True
            try:
                db.session.delete(enrolment)
                db.session.commit()

                print(cls.get_enrolments_by_league_id(league_id))
                return cls.get_enrolments_by_league_id(league_id)
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise EnrolmentException

    @classmethod
    def get_enrolments_table_by_league_id(cls, league_id: int) -> list[dict[str, Any]]:
        """
        Return an existing enrolment
        :param league_id:
        :return:
        """
        enrolments = db.session.query(Enrolment).filter_by(league_id=league_id).order_by(desc(Enrolment.points)).all()

        if enrolments:
            serialized_enrolments = []
            id = 1
            for enrolment in enrolments:
                user = User.get_user_by_id(enrolment.user_id)

                serialized_enrolment = {
                    "id": id,
                    "name": user.name,
                    "points": enrolment.points,
                    "wins": enrolment.wins,
                    "defeats": enrolment.defeats
                }

                serialized_enrolments.append(serialized_enrolment)
                id += 1

            return serialized_enrolments
        else:
            raise EnrolmentLeagueIdException
