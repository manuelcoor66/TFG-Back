import datetime

from sqlalchemy import or_, Date, and_
from typing import Any

from src.models import db
from src.models.enrolments import Enrolment
from src.models.league import League
from src.models.matches.matches_exception import UserWithMatch, MatchesLeagueIdException
from src.models.sports import Sports
from src.models.user import User


class Matches(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer)
    result = db.Column(db.String(length=50))
    player_id_1 = db.Column(db.Integer)
    player_id_2 = db.Column(db.Integer)
    player_id_3 = db.Column(db.Integer, default=None)
    player_id_4 = db.Column(db.Integer, default=None)
    date = db.Column(db.DateTime)
    place = db.Column(db.Integer)

    def __init__(
        self,
        league_id,
        result,
        player_id_1,
        player_id_2,
        player_id_3=None,
        player_id_4=None,
        date=None,
        place=None,
    ):
        self.league_id = league_id
        self.result = result
        self.player_id_1 = player_id_1
        self.player_id_2 = player_id_2
        self.player_id_3 = player_id_3
        self.player_id_4 = player_id_4
        self.date = date
        self.place = place

    def __repr__(self):
        return (
            f"<Match(id={self.id}, league_id={self.league_id}, result='{self.result}')"
        )

    @classmethod
    def get_matches_list_by_league_id(cls, league_id: int) -> list[dict[str, Any]]:
        matches = db.session.query(Matches).filter_by(league_id=league_id).all()

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    "id": match.id,
                    "league_id": match.league_id,
                    "result": match.result,
                    "player_name_1": User.get_user_by_id(match.player_id_1).name
                    + " "
                    + User.get_user_by_id(match.player_id_1).last_names,
                    "player_name_2": User.get_user_by_id(match.player_id_2).name
                    + " "
                    + User.get_user_by_id(match.player_id_2).last_names,
                    "date": match.date,
                    "place": match.place,
                }

                if match.player_id_3 != 0:
                    serialized_match["player_name_3"] = (
                        User.get_user_by_id(match.player_id_3).name
                        + " "
                        + User.get_user_by_id(match.player_id_3).last_names
                    )

                if match.player_id_4 != 0:
                    serialized_match["player_name_4"] = (
                        User.get_user_by_id(match.player_id_4).name
                        + " "
                        + User.get_user_by_id(match.player_id_4).last_names
                    )

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_finalized_user_matches(cls, user_id: int) -> list[dict[str, Any]]:
        matches = (
            db.session.query(Matches)
            .filter(
                or_(
                    Matches.player_id_1 == user_id,
                    Matches.player_id_2 == user_id,
                    Matches.player_id_3 == user_id,
                    Matches.player_id_4 == user_id,
                ),
                Matches.date < datetime.datetime.now(),
            )
            .all()
        )

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    "id": match.id,
                    "league_id": match.league_id,
                    "result": match.result,
                    "player_name_1": User.get_user_by_id(match.player_id_1).name
                    + " "
                    + User.get_user_by_id(match.player_id_1).last_names,
                    "player_name_2": User.get_user_by_id(match.player_id_2).name
                    + " "
                    + User.get_user_by_id(match.player_id_2).last_names,
                    "date": match.date,
                    "place": match.place,
                }

                if match.player_id_3 != 0:
                    serialized_match["player_name_3"] = (
                        User.get_user_by_id(match.player_id_3).name
                        + " "
                        + User.get_user_by_id(match.player_id_3).last_names
                    )

                if match.player_id_4 != 0:
                    serialized_match["player_name_4"] = (
                        User.get_user_by_id(match.player_id_4).name
                        + " "
                        + User.get_user_by_id(match.player_id_4).last_names
                    )

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_active_user_matches(cls, user_id: int) -> list[dict[str, Any]]:
        matches = (
            db.session.query(Matches)
            .filter(
                or_(
                    Matches.player_id_1 == user_id,
                    Matches.player_id_2 == user_id,
                    Matches.player_id_3 == user_id,
                    Matches.player_id_4 == user_id,
                ),
                Matches.date > datetime.datetime.now(),
            )
            .all()
        )

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    "id": match.id,
                    "league_id": match.league_id,
                    "result": match.result,
                    "player_name_1": User.get_user_by_id(match.player_id_1).name
                    + " "
                    + User.get_user_by_id(match.player_id_1).last_names,
                    "player_name_2": User.get_user_by_id(match.player_id_2).name
                    + " "
                    + User.get_user_by_id(match.player_id_2).last_names,
                    "date": match.date,
                    "place": match.place,
                }

                if match.player_id_3 != 0:
                    serialized_match["player_name_3"] = (
                        User.get_user_by_id(match.player_id_3).name
                        + " "
                        + User.get_user_by_id(match.player_id_3).last_names
                    )

                if match.player_id_4 != 0:
                    serialized_match["player_name_4"] = (
                        User.get_user_by_id(match.player_id_4).name
                        + " "
                        + User.get_user_by_id(match.player_id_4).last_names
                    )

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_finalized_league_matches(cls, league_id: int) -> list[dict[str, Any]]:
        matches = (
            db.session.query(Matches)
            .filter(
                Matches.date < datetime.datetime.now(), Matches.league_id == league_id
            )
            .all()
        )

        league = db.session.query(League).filter_by(id=league_id).first()
        sport = db.session.query(Sports).filter_by(id=league.sport_id).first()

        if matches:
            serialized_matches = []
            for match in matches:
                players = 2
                serialized_match = {
                    "id": match.id,
                    "league_id": match.league_id,
                    "result": match.result,
                    "player_name_1": User.get_user_by_id(match.player_id_1).name
                    + " "
                    + User.get_user_by_id(match.player_id_1).last_names,
                    "player_name_2": User.get_user_by_id(match.player_id_2).name
                    + " "
                    + User.get_user_by_id(match.player_id_2).last_names,
                    "date": match.date,
                    "place": match.place,
                }

                if match.player_id_3 != 0:
                    players+=1
                    serialized_match["player_name_3"] = (
                        User.get_user_by_id(match.player_id_3).name
                        + " "
                        + User.get_user_by_id(match.player_id_3).last_names
                    )

                if match.player_id_4 != 0:
                    players+=1
                    serialized_match["player_name_4"] = (
                        User.get_user_by_id(match.player_id_4).name
                        + " "
                        + User.get_user_by_id(match.player_id_4).last_names
                    )

                if sport.players is players:
                    serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise MatchesLeagueIdException

    @classmethod
    def get_active_league_matches(cls, league_id: int) -> list[dict[str, Any]]:
        matches = (
            db.session.query(Matches)
            .filter(
                Matches.date > datetime.datetime.now(), Matches.league_id == league_id
            )
            .all()
        )

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    "id": match.id,
                    "league_id": match.league_id,
                    "result": match.result,
                    "player_name_1": User.get_user_by_id(match.player_id_1).name
                    + " "
                    + User.get_user_by_id(match.player_id_1).last_names,
                    # "player_name_2": User.get_user_by_id(match.player_id_2).name
                    # + " "
                    # + User.get_user_by_id(match.player_id_2).last_names,
                    "date": match.date,
                    "place": match.place,
                }

                if match.player_id_2 != 0:
                    serialized_match["player_name_2"] = (
                        User.get_user_by_id(match.player_id_2).name
                        + " "
                        + User.get_user_by_id(match.player_id_2).last_names
                    )

                if match.player_id_3 != 0:
                    serialized_match["player_name_3"] = (
                        User.get_user_by_id(match.player_id_3).name
                        + " "
                        + User.get_user_by_id(match.player_id_3).last_names
                    )

                if match.player_id_4 != 0:
                    serialized_match["player_name_4"] = (
                        User.get_user_by_id(match.player_id_4).name
                        + " "
                        + User.get_user_by_id(match.player_id_4).last_names
                    )

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            return {}

    @classmethod
    def create_league(cls, league_id: int, player_id_1: int, date: Date, place: int):
        matches = (
            db.session.query(Matches)
            .filter(
                Matches.league_id == league_id,
                or_(
                    Matches.player_id_1 == player_id_1,
                    Matches.player_id_2 == player_id_1,
                    Matches.player_id_3 == player_id_1,
                    Matches.player_id_4 == player_id_1,
                ),
                Matches.date > datetime.datetime.now(),
            )
            .all()
        )
        if not matches:
            new_match = Matches(
                league_id=league_id,
                result="",
                player_id_1=player_id_1,
                player_id_2=0,
                player_id_3=0,
                player_id_4=0,
                date=date,
                place=place,
            )

            try:
                db.session.add(new_match)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

            return new_match
        else:
            raise UserWithMatch

    @classmethod
    def add_new_player(cls, match_id: int, player_id: int):
        match = (
            db.session.query(Matches)
            .filter(
                Matches.date > datetime.datetime.now(),
                Matches.id == match_id,
                and_(
                    Matches.player_id_1 != player_id,
                    Matches.player_id_2 != player_id,
                    Matches.player_id_3 != player_id,
                    Matches.player_id_4 != player_id,
                    or_(
                        Matches.player_id_1 == 0,
                        Matches.player_id_2 == 0,
                        Matches.player_id_3 == 0,
                        Matches.player_id_4 == 0,
                    ),
                ),
            )
            .first()
        )

        if match:
            if match.player_id_1 == 0:
                match.player_id_1 = player_id
            elif match.player_id_2 == 0:
                match.player_id_2 = player_id
            elif match.player_id_3 == 0:
                match.player_id_3 = player_id
            else:
                match.player_id_4 = player_id

            try:
                db.session.commit()

                return match
            except Exception as e:
                db.session.rollback()
                raise e

        else:
            raise Exception("No existen partidos.")

    @classmethod
    def add_result(
        cls,
        match_id: int,
        result: str,
        win_player_1: bool,
        win_player_2: bool,
        win_player_3: bool,
        win_player_4: bool,
    ):
        match = (
            db.session.query(Matches)
            .filter(
                Matches.date < datetime.datetime.now(),
                Matches.id == match_id,
                and_(
                    Matches.player_id_1 != 0,
                    Matches.player_id_2 != 0,
                    Matches.player_id_3 != 0,
                    Matches.player_id_4 != 0,
                ),
            )
            .first()
        )

        if match:
            match.result = result

            Enrolment.add_result(match.player_id_1, match.league_id, win_player_1)
            Enrolment.add_result(match.player_id_2, match.league_id, win_player_2)
            if win_player_3 != "null" and win_player_4 != "null":
                Enrolment.add_result(match.player_id_3, match.league_id, win_player_3)
                Enrolment.add_result(match.player_id_4, match.league_id, win_player_4)

            try:
                db.session.commit()

                return match
            except Exception as e:
                db.session.rollback()
                raise e

        else:
            raise Exception("No existe el partidos.")
