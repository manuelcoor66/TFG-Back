import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.matches import (
    Matches,
    MatchesListSchema,
    MatchResponse,
    CreateMatchSchema,
    AddNewPlayerSchema,
    MatchAddResponse,
    AddResultSchema,
)
from src.models.matches.matches_exception import MatchesLeagueIdException
from src.models.user.user_exception import UserIdException

api_url = "/matches"
api_name = "Matches"
api_description = "Matches service"

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
@blp.response(200, MatchesListSchema)
def get_matches_by_league_id(league_id: int):
    """
    Get all the matches of a league
    """
    try:
        matches = Matches.get_matches_list_by_league_id(league_id)

        return {"items": matches, "total": len(matches)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/finalized/<int:user_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, MatchesListSchema)
def get_finalized_matches_by_user_id(user_id: int):
    """
    Get the finalized matches of a user
    """
    try:
        matches = Matches.get_finalized_user_matches(user_id)

        return {"items": matches, "total": len(matches)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/active/<int:user_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, MatchesListSchema)
def get_active_matches_by_user_id(user_id: int):
    """
    Get the active matches of a user
    """
    try:
        matches = Matches.get_active_user_matches(user_id)

        return {"items": matches, "total": len(matches)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/finalized/league/<int:league_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, MatchesListSchema)
def get_finalized_matches_by_league_id(league_id: int):
    """
    Get the finalized matches of a league
    """
    try:
        matches = Matches.get_finalized_league_matches(league_id)

        return {"items": matches, "total": len(matches)}
    except (MatchesLeagueIdException, UserIdException) as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/active/league/<int:league_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, MatchesListSchema)
def get_active_matches_by_league_id(league_id: int):
    """
    Get the active matches of a league
    """
    try:
        matches = Matches.get_active_league_matches(league_id)

        return {"items": matches, "total": len(matches)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/create", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(CreateMatchSchema, location="query")
@blp.response(200, MatchResponse)
def create_league(data):
    """
    Create a new match
    """
    try:
        new_match = Matches.create_league(
            data.get("league_id"),
            data.get("player_name_1"),
            data.get("date"),
            data.get("place"),
        )

        return new_match
    except Exception as e:
        return {"message": str(e)}


@blp.route("/add-player", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(AddNewPlayerSchema, location="query")
@blp.response(200, MatchAddResponse)
def add_player(data):
    """
    Add new player to a match
    """
    try:
        match = Matches.add_new_player(
            data.get("match_id"),
            data.get("player_id"),
        )

        return match
    except Exception as e:
        return {"message": str(e)}


@blp.route("/add-result", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(AddResultSchema, location="query")
@blp.response(200, MatchAddResponse)
def add_result(data):
    """
    Add a result to a match
    """
    try:
        match = Matches.add_result(
            data.get("match_id"),
            data.get("result"),
        )

        return match
    except Exception as e:
        return {"message": str(e)}
