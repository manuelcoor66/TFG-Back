import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.places import (
    Places,
    PlaceReturnSchema,
    PlaceReturnListSchema,
    PlaceInputSchema,
    PlaceInputModifySchema,
)

from src.models.places.places_exception import (
    PlaceIdException,
    PlaceNameException,
    PlaceNameExistsException,
)

api_url = "/places"
api_name = "Places"
api_description = "Places service"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)


@blp.route("/<int:place_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, PlaceReturnSchema)
def get_place_by_id(place_id: int):
    """
    Get a place by his id
    """
    try:
        place = Places.get_place_by_id(place_id)

        return place
    except PlaceIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/<string:name>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, PlaceReturnSchema)
def get_place_by_name(name: str):
    """
    Get a place by his name
    """
    try:
        place = Places.get_place_by_name(name)

        return place
    except PlaceNameException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/all-places", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, PlaceReturnListSchema)
def get_all_places():
    """
    Get all the places
    """
    try:
        places = Places.get_all_places()

        return {"items": places, "total": len(places)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/create", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(PlaceInputSchema, location="query")
@blp.response(200, PlaceReturnSchema)
def create_place(data):
    """
    Creates a new place
    """
    try:
        new_place = Places.add_new_place(data.get("name"), data.get("coordinates"))

        return new_place
    except PlaceNameExistsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/modify", methods=["PATCH"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(PlaceInputModifySchema, location="query")
@blp.response(200, PlaceReturnSchema)
def modify_place(data):
    """
    Modifies a place
    """
    try:
        new_place = Places.modify_place(
            data.get("id"), data.get("name"), data.get("coordinates")
        )

        return new_place
    except PlaceIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response
