import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.matches import (
    Matches,
    MatchesListSchema
)



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
def get_matches_by_league_id(user_id: int):
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
def get_matches_by_league_id(user_id: int):
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
def get_matches_by_league_id(league_id: int):
    """
    Get the finalized matches of a league
    """
    try:
        matches = Matches.get_finalized_league_matches(league_id)

        return {"items": matches, "total": len(matches)}
    except Exception as e:
        return {"message": str(e)}


@blp.route("/active/league/<int:league_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, MatchesListSchema)
def get_matches_by_league_id(league_id: int):
    """
    Get the active matches of a league
    """
    try:
        matches = Matches.get_active_league_matches(league_id)

        return {"items": matches, "total": len(matches)}
    except Exception as e:
        return {"message": str(e)}
