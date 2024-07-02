from datetime import date
from typing import Any

from src.models.league.league_exceptions import (
    LeagueExistsException,
    LeagueIdException,
    LeagueNameException,
)

from src.models import db
from src.models.user import User


class League(db.Model):
    __tablename__ = "league"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    created_by = db.Column(db.Integer)
    enrolments = db.Column(db.Integer)
    points_victory = db.Column(db.Integer, nullable=True)
    points_defeat = db.Column(db.Integer, nullable=True)
    weeks = db.Column(db.Integer, nullable=True)
    weeks_played = db.Column(db.Integer, nullable=True)
    date_start = db.Column(db.Date, nullable=True)

    def __init__(
        self,
        name,
        description,
        created_by,
        enrolments,
        points_victory,
        points_defeat,
        weeks,
        weeks_played,
        date_start,
    ):
        self.name = name
        self.description = description
        self.created_by = created_by
        self.enrollments = enrolments
        self.points_victory = points_victory
        self.points_defeat = points_defeat
        self.weeks = weeks
        self.weeks_played = weeks_played
        self.date_start = date_start

    def __repr__(self) -> str:
        """
        String representation of a league
        """
        return f"<League {self.name}>"

    @classmethod
    def get_league_by_id(cls, league_id: int) -> "League":
        """
        Get an existing league
        :param league_id:
        :return: The searched league
        """
        league = db.session.query(League).filter_by(id=league_id).first()

        if league:
            user = User.get_user_by_id(league.created_by)
            league.created_by_id = league.created_by
            league.created_by = user.name + ' ' + user.last_names

            return league
        else:
            raise LeagueIdException

    @classmethod
    def get_league_by_name(cls, league_name: str) -> "League":
        """
        Get an existing league
        :param league_name:
        :return: The searched league
        """
        league = db.session.query(League).filter_by(name=league_name).first()

        if league:
            user = User.get_user_by_id(league.created_by)
            league.created_by_id = league.created_by
            league.created_by = user.name + ' ' + user.last_names

            return league
        else:
            raise LeagueNameException

    @classmethod
    def get_all_leagues(cls) -> list[dict[str, Any]]:
        leagues = db.session.query(League).all()

        if leagues:
            serialized_leagues = []
            for league in leagues:
                user = User.get_user_by_id(league.created_by)

                serialized_league = {
                    "id": league.id,
                    "name": league.name,
                    "description": league.description,
                    "created_by": user.name + ' ' + user.last_names,
                    "created_by_id": league.created_by,
                    "enrolments": league.enrolments,
                    "points_victory": league.points_victory,
                    "points_defeat": league.points_defeat,
                    "weeks": league.weeks,
                    "weeks_played": league.weeks_played,
                    "date_start": league.date_start,
                }

                serialized_leagues.append(serialized_league)

            return serialized_leagues
        else:
            raise Exception("No existen usuarios.")

    @classmethod
    def create_league(
        cls,
        name: str,
        description: str,
        created_by: int,
        points_victory: int,
        points_defeat: int,
        weeks: int,
        date_start: date,
    ) -> "League":
        """
        Create a new league
        :param name:
        :param description:
        :param created_by:
        :param points_victory:
        :param points_defeat:
        :param weeks:
        :param date_start:
        :return: The new league
        """
        league = db.session.query(League).filter_by(name=name).first()

        if league is None:
            new_league = League(
                name=name,
                description=description,
                created_by=created_by,
                enrolments=0,
                points_victory=points_victory,
                points_defeat=points_defeat,
                weeks=weeks,
                weeks_played=0,
                date_start=date_start,
            )
            try:
                db.session.add(new_league)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

            return new_league
        else:
            raise LeagueExistsException

    @classmethod
    def delete_league_by_id(cls, league_id: int) -> None:
        """
        Delete an existing league
        :param league_id:
        """
        league = cls.get_league_by_id(league_id)

        if league:
            try:
                db.session.delete(league)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise LeagueIdException

    @classmethod
    def delete_league_by_name(cls, league_name: str) -> None:
        """
        Delete an existing league
        :param league_name:
        """
        league = cls.get_league_by_name(league_name)
        print(league.name)

        if league:
            try:
                db.session.delete(league)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise LeagueIdException

    @classmethod
    def modify_league(
        cls,
        id: int,
        name: str,
        description: str,
        points_victory: int,
        points_defeat: int,
        weeks: int,
        date_start: date,
    ) -> "League":
        """
        Modify an existing league
        :param id:
        :param name:
        :param description:
        :param points_victory:
        :param points_defeat:
        :param weeks:
        :param date_start:
        :return: The updated league
        """
        league = cls.get_league_by_id(id)

        if league is not None:
            league.name = name
            if description:
                league.description = description

            if league.date_start is not None and league.date_start > date.today():
                league.date_start = date_start
                league.points_victory = points_victory
                league.points_defeat = points_defeat
                league.weeks = weeks

            try:
                db.session.commit()
                return league
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise LeagueNameException

    @classmethod
    def finalize_league(cls, league_id: int) -> None:
        """
        Finalize an existing league
        :param league_id:
        """
        league = cls.get_league_by_id(league_id)

        if league:
            try:
                league.weeks_played = league.weeks
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise LeagueIdException
