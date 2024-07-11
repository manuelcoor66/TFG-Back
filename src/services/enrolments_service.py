import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.enrolments import (
    EnrolmentListSchema,
    EnrolmentInputSchema,
    CreateEnrolmentSchema,
    AddMatchSchema,
    EnrolmentSchema,
    EnrolmentsLeagueTableListSchema,
)
from src.models.enrolments.enrolments import Enrolment
from src.models.enrolments.enrolments_exceptions import (
    EnrolmentIdException,
    EnrolmentUserIdException,
    EnrolmentLeagueIdException,
    EnrolmentsException,
    EnrolmentException,
)
from src.models.league.league_exceptions import LeagueIdException

api_url = "/enrolments"
api_name = "Enrolments"
api_description = "Enrolments service"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)


@blp.route("/<int:enrolment_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, EnrolmentInputSchema)
def get_enrolment_by_id(enrolment_id: int):
    """
    Get an enrolment by his id
    """
    try:
        league = Enrolment.get_enrolment_by_id(enrolment_id)
        return league
    except EnrolmentIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/user/<int:user_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, EnrolmentListSchema)
def get_enrolment_by_user_id(user_id: int):
    """
    Get an user enrolments by his id
    """
    try:
        enrolments = Enrolment.get_enrolments_by_user_id(user_id)

        return {"items": enrolments, "total": len(enrolments)}
    except EnrolmentUserIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/league/<int:league_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, EnrolmentListSchema)
def get_enrolment_by_league_id(league_id: int):
    """
    Get a league enrolments by his id
    """
    try:
        enrolments = Enrolment.get_enrolments_by_league_id(league_id)

        return {"items": enrolments, "total": len(enrolments)}
    except EnrolmentLeagueIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/list", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, EnrolmentListSchema)
def get_all_enrolments():
    """
    Get all the enrolments
    """
    try:
        enrolments = Enrolment.get_all_enrolments()

        return {"items": enrolments, "total": len(enrolments)}
    except EnrolmentsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/create_enrolment", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(CreateEnrolmentSchema, location="query")
@blp.response(200, EnrolmentInputSchema)
def create_enrolment(data):
    """
    Create a new enrolment
    """
    try:
        new_enrolment = Enrolment.add_new_enrolment(
            data.get("user_id"), data.get("league_id"), data.get("points")
        )
        return new_enrolment
    except Exception as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/add_match", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(AddMatchSchema, location="query")
@blp.response(200, EnrolmentListSchema)
def add_match(data):
    """
    Add a new match to an enrolment
    """
    try:
        enrolments = Enrolment.add_new_match(
            data.get("user_id"), data.get("league_id"), data.get("win")
        )

        return {"items": enrolments, "total": len(enrolments)}
    except (LeagueIdException, EnrolmentException, Exception) as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/finalize_enrolment", methods=["PUT"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(EnrolmentSchema, location="query")
@blp.response(200, EnrolmentListSchema)
def finalize_enrolment(data):
    """
    Finalize an enrolment
    """
    try:
        enrolments = Enrolment.finalize_enrolment(data.get("user_id"), data.get("league_id"))

        return {"items": enrolments, "total": len(enrolments)}
    except EnrolmentException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/table/<int:league_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, EnrolmentsLeagueTableListSchema)
def get_enrolment_by_league_id(league_id: int):
    """
    Get a league enrolments by his id to show
    """
    try:
        enrolments = Enrolment.get_enrolments_table_by_league_id(league_id)

        return {"items": enrolments, "total": len(enrolments)}
    except EnrolmentLeagueIdException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response
