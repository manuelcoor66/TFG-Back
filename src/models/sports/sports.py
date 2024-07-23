from typing import Any

from src.models import db
from src.models.sports.sports_exception import (
    SportNameException,
    SportIdException,
    SportException,
    SportNameExistsException,
)


class Sports(db.Model):
    __tablename__ = "sports"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    icon = db.Column(db.String(20))
    players = db.Column(db.Integer)

    def __init__(self, name, icon, players):
        self.name = name
        self.icon = icon
        self.players = players

    def __repr__(self):
        return f"<Sports(id={self.id}, name={self.name}, icon={self.icon}, players={self.players})>"

    @classmethod
    def get_sports_by_id(cls, id: int) -> "Sports":
        sport = db.session.query(Sports).filter_by(id=id).first()

        if sport:
            return sport
        else:
            raise SportIdException

    @classmethod
    def get_sports_by_name(cls, name: str) -> "Sports":
        sport = db.session.query(Sports).filter_by(name=name).first()

        if sport:
            return sport
        else:
            raise SportNameException

    @classmethod
    def get_all_sports(cls) -> "list[dict[str, Any]]":
        sports = db.session.query(Sports).all()

        if sports:
            serialized_sports = []
            for sport in sports:
                serialized_sport = {
                    "id": sport.id,
                    "name": sport.name,
                    "icon": sport.icon,
                    "players": sport.players,
                }
                serialized_sports.append(serialized_sport)

            return serialized_sports

        else:
            raise SportException

    @classmethod
    def add_new_sport(cls, name: str, icon: str, players: int) -> "Sports":
        new_sport = Sports(name=name, icon=icon, players=players)
        sport = db.session.query(Sports).filter_by(name=name).first()

        if not sport:
            try:
                db.session.add(new_sport)
                db.session.commit()

                return new_sport
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise SportNameExistsException
