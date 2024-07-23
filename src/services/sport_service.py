import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.sports import Sports, SportsSchema, SportsListSchema, CreateSportSchema
from src.models.sports.sports_exception import SportIdException, SportNameException, SportException, \
    SportNameExistsException

api_url = "/sports"
api_name = "Sports"
api_description = "Sports service"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)

@blp.route("/<int:sport_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, SportsSchema)
def get_sport_by_id(sport_id: int):
    """
    Get a sport by id
    """
    try:
        sport = Sports.get_sports_by_id(sport_id)

        return sport
    except SportIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/<string:sport_name>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, SportsSchema)
def get_sport_by_name(sport_name: str):
    """
    Get a sport by name
    """
    try:
        sport = Sports.get_sports_by_name(sport_name)

        return sport
    except SportNameException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/all-sports", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, SportsListSchema)
def get_place_by_id():
    """
    Get all the places
    """
    try:
        sports = Sports.get_all_sports()

        return {"items": sports, "total": len(sports)}
    except SportException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/create", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(CreateSportSchema, location="query")
@blp.response(200, SportsSchema)
def create_place(data):
    """
    Creates a new sport
    """
    try:
        new_place = Sports.add_new_sport(
            data.get("name"), data.get("icon"), data.get("players")
        )

        return new_place
    except SportNameExistsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response
