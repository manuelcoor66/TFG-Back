import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.league import (
    League,
    LeagueInputSchema,
    LeagueListSchema,
    CreateLeagueSchema,
    ModifyLeagueInputSchema,
    LeagueIdSchema,
)
from src.models.league.league_exceptions import (
    LeagueExistsException,
    LeagueIdException,
    LeagueNameException,
)

api_url = "/league"
api_name = "League"
api_description = "League service"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)


@blp.route("/<int:league_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, LeagueInputSchema)
def get_league_by_id(league_id: int):
    """
    Get a league by his id
    """
    try:
        league = League.get_league_by_id(league_id)
        return league
    except LeagueIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/name/<string:league_name>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, LeagueInputSchema)
def get_league_by_name(league_name: str):
    """
    Get a league by his name
    """
    try:
        new_user = League.get_league_by_name(league_name)
        return new_user
    except LeagueNameException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/league_list", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, LeagueListSchema)
def get_all_leagues():
    """
    Get all the leagues
    """
    try:
        leagues = League.get_all_leagues()

        return {"items": leagues, "total": len(leagues)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/create-league", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(CreateLeagueSchema, location="query")
@blp.response(200, LeagueInputSchema)
def create_league(data):
    """
    Create a new league
    """
    try:
        new_user = League.create_league(
            data.get("name"),
            data.get("description"),
            data.get("created_by"),
            data.get("points_victory"),
            data.get("points_defeat"),
            data.get("weeks"),
            data.get("date_start"),
        )
        return new_user
    except (LeagueExistsException, Exception) as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/<int:league_id>", methods=["DELETE"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200)
def delete_league_by_id(league_id: int):
    """
    Delete a league by his id
    """
    try:
        League.delete_league_by_id(league_id)
    except LeagueIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/<string:league_name>", methods=["DELETE"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200)
def delete_league_by_name(league_name: str):
    """
    Delete a league by his name
    """
    try:
        League.delete_league_by_name(league_name)
    except LeagueNameException as e:
        response = jsonify({"error": str(e)})
        response.status_code = 422
        return response


@blp.route("/modify-league", methods=["PATCH"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(ModifyLeagueInputSchema, location="query")
@blp.response(200, LeagueInputSchema)
def modify_league(data):
    """
    Modify an existing user
    """
    try:
        new_user = League.modify_league(
            data.get("id"),
            data.get("name"),
            data.get("description"),
            data.get("points_victory"),
            data.get("points_defeat"),
            data.get("weeks"),
            data.get("date_start"),
        )
        return new_user
    except (LeagueIdException, Exception) as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/finalize-league", methods=["PUT"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(LeagueIdSchema, location="query")
@blp.response(200)
def finalize_league(data):
    try:
        League.finalize_league(data.get("id"))
    except (LeagueIdException, Exception) as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response
