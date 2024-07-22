import datetime

from sqlalchemy import or_
from typing import Any

from src.models import db
from src.models.user import User


class Matches(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer)
    result = db.Column(db.String(length=50))
    player_id_1 = db.Column(db.Integer)
    player_id_2 = db.Column(db.Integer)
    player_id_3 = db.Column(db.Integer, default=None)
    player_id_4 = db.Column(db.Integer, default=None)
    date = db.Column(db.DateTime)
    place = db.Column(db.Integer)

    def __init__(self, league_id, result, player_id_1, player_id_2, player_id_3=None, player_id_4=None, date=None,
                 place=None):
        self.league_id = league_id
        self.result = result
        self.player_id_1 = player_id_1
        self.player_id_2 = player_id_2
        self.player_id_3 = player_id_3
        self.player_id_4 = player_id_4
        self.date = date
        self.place = place

    def __repr__(self):
        return f"<Match(id={self.id}, league_id={self.league_id}, result='{self.result}'"

    @classmethod
    def get_matches_list_by_league_id(cls, league_id: int) -> list[dict[str, Any]]:
        matches = db.session.query(Matches).filter_by(league_id=league_id).all()

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    'id': match.id,
                    'league_id': match.league_id,
                    'result': match.result,
                    'player_name_1': User.get_user_by_id(match.player_id_1).name + ' ' + User.get_user_by_id(match.player_id_1).last_names,
                    'player_name_2': User.get_user_by_id(match.player_id_2).name + ' ' + User.get_user_by_id(match.player_id_2).last_names,
                    'date': match.date,
                    'place': match.place
                }

                if match.player_id_3 != 0:
                    serialized_match['player_name_3'] = User.get_user_by_id(match.player_id_3).name + ' ' + User.get_user_by_id(match.player_id_3).last_names

                if match.player_id_4 != 0:
                    serialized_match['player_name_4'] = User.get_user_by_id(match.player_id_4).name + ' ' + User.get_user_by_id(match.player_id_4).last_names

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_finalized_user_matches(cls, user_id: int) -> list[dict[str, Any]]:
        matches = db.session.query(Matches).filter(
            or_(
                Matches.player_id_1 == user_id,
                Matches.player_id_2 == user_id,
                Matches.player_id_3 == user_id,
                Matches.player_id_4 == user_id
            ),
            Matches.date < datetime.datetime.now()
        ).all()

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    'id': match.id,
                    'league_id': match.league_id,
                    'result': match.result,
                    'player_name_1': User.get_user_by_id(match.player_id_1).name + ' ' + User.get_user_by_id(match.player_id_1).last_names,
                    'player_name_2': User.get_user_by_id(match.player_id_2).name + ' ' + User.get_user_by_id(match.player_id_2).last_names,
                    'date': match.date,
                    'place': match.place
                }

                if match.player_id_3 != 0:
                    serialized_match['player_name_3'] = User.get_user_by_id(match.player_id_3).name + ' ' + User.get_user_by_id(match.player_id_3).last_names

                if match.player_id_4 != 0:
                    serialized_match['player_name_4'] = User.get_user_by_id(match.player_id_4).name + ' ' + User.get_user_by_id(match.player_id_4).last_names

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_active_user_matches(cls, user_id: int) -> list[dict[str, Any]]:
        matches = db.session.query(Matches).filter(
            or_(
                Matches.player_id_1 == user_id,
                Matches.player_id_2 == user_id,
                Matches.player_id_3 == user_id,
                Matches.player_id_4 == user_id
            ),
            Matches.date > datetime.datetime.now()
        ).all()

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    'id': match.id,
                    'league_id': match.league_id,
                    'result': match.result,
                    'player_name_1': User.get_user_by_id(match.player_id_1).name + ' ' + User.get_user_by_id(match.player_id_1).last_names,
                    'player_name_2': User.get_user_by_id(match.player_id_2).name + ' ' + User.get_user_by_id(match.player_id_2).last_names,
                    'date': match.date,
                    'place': match.place
                }

                if match.player_id_3 != 0:
                    serialized_match['player_name_3'] = User.get_user_by_id(match.player_id_3).name + ' ' + User.get_user_by_id(match.player_id_3).last_names

                if match.player_id_4 != 0:
                    serialized_match['player_name_4'] = User.get_user_by_id(match.player_id_4).name + ' ' + User.get_user_by_id(match.player_id_4).last_names

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_finalized_league_matches(cls, league_id: int) -> list[dict[str, Any]]:
        matches = db.session.query(Matches).filter(
            Matches.date < datetime.datetime.now(),
            Matches.league_id == league_id
        ).all()

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    'id': match.id,
                    'league_id': match.league_id,
                    'result': match.result,
                    'player_name_1': User.get_user_by_id(match.player_id_1).name + ' ' + User.get_user_by_id(match.player_id_1).last_names,
                    'player_name_2': User.get_user_by_id(match.player_id_2).name + ' ' + User.get_user_by_id(match.player_id_2).last_names,
                    'date': match.date,
                    'place': match.place
                }

                if match.player_id_3 != 0:
                    serialized_match['player_name_3'] = User.get_user_by_id(match.player_id_3).name + ' ' + User.get_user_by_id(match.player_id_3).last_names

                if match.player_id_4 != 0:
                    serialized_match['player_name_4'] = User.get_user_by_id(match.player_id_4).name + ' ' + User.get_user_by_id(match.player_id_4).last_names

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")

    @classmethod
    def get_active_league_matches(cls, league_id: int) -> list[dict[str, Any]]:
        matches = db.session.query(Matches).filter(
            Matches.date > datetime.datetime.now(),
            Matches.league_id == league_id
        ).all()

        if matches:
            serialized_matches = []
            for match in matches:
                serialized_match = {
                    'id': match.id,
                    'league_id': match.league_id,
                    'result': match.result,
                    'player_name_1': User.get_user_by_id(match.player_id_1).name + ' ' + User.get_user_by_id(match.player_id_1).last_names,
                    'player_name_2': User.get_user_by_id(match.player_id_2).name + ' ' + User.get_user_by_id(match.player_id_2).last_names,
                    'date': match.date,
                    'place': match.place
                }

                if match.player_id_3 != 0:
                    serialized_match['player_name_3'] = User.get_user_by_id(match.player_id_3).name + ' ' + User.get_user_by_id(match.player_id_3).last_names

                if match.player_id_4 != 0:
                    serialized_match['player_name_4'] = User.get_user_by_id(match.player_id_4).name + ' ' + User.get_user_by_id(match.player_id_4).last_names

                serialized_matches.append(serialized_match)

            return serialized_matches
        else:
            raise Exception("No existen partidos.")
