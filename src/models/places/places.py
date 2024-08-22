from typing import Any

from src.models import db
from src.models.places.places_exception import (
    PlaceIdException,
    PlaceNameException,
    PlaceNameExistsException,
)


class Places(db.Model):
    __tablename__ = "places"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    coordinates = db.Column(db.String(80), unique=True)

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def __repr__(self):
        return (
            f"<Places(id={self.id}, name={self.name}, coordinates={self.coordinates})>"
        )

    @classmethod
    def get_place_by_id(cls, id: int) -> "Places":
        place = db.session.query(Places).filter_by(id=id).first()

        if place:
            return place
        else:
            raise PlaceIdException

    @classmethod
    def get_place_by_name(cls, name: str) -> "Places":
        place = db.session.query(Places).filter_by(name=name).first()

        if place:
            return place
        else:
            raise PlaceNameException

    @classmethod
    def get_all_places(cls) -> "list[dict[str, Any]]":
        places = db.session.query(Places).all()

        if places:
            serialized_places = []
            for place in places:
                serialized_place = {
                    "id": place.id,
                    "name": place.name,
                    "coordinates": place.coordinates,
                }
                serialized_places.append(serialized_place)

            return serialized_places
        else:
            raise Exception("No existen places.")

    @classmethod
    def add_new_place(cls, name: str, coordinates: str) -> "Places":
        new_place = Places(name=name, coordinates=coordinates)
        place = db.session.query(Places).filter_by(name=name).first()

        if not place:
            try:
                db.session.add(new_place)
                db.session.commit()

                return new_place
            except Exception as e:
                db.session.rollback()
                raise e
        else:
            raise PlaceNameExistsException

    @classmethod
    def modify_place(cls, id: int, name: str, coordinates: str):
        place = cls.get_place_by_id(id)

        if name:
            place.name = name
        if coordinates:
            place.coordinates = coordinates

        try:
            db.session.commit()
            return place
        except Exception as e:
            db.session.rollback()
            raise e
