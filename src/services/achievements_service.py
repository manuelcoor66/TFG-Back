import flask
from flask import jsonify
from flask_smorest import Blueprint

from src.models.achievements import (
    Achievements,
    AchievementsListSchema,
    CreateAchievementSchema,
    AchievementsInputSchema,
    UserAchievementsListSchema,
)
from src.models.achievements.achievements_exceptions import (
    AchievementsException,
    AchievementExistsException,
)

api_url = "/achievements"
api_name = "Achievements"
api_description = "Achievements service"

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)


@blp.route("/list", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, AchievementsListSchema)
def get_all_enrolments():
    """
    Get all the achievements
    """
    try:
        achievements = Achievements.get_all_achievements()

        return {"items": achievements, "total": len(achievements)}
    except AchievementsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response


@blp.route("/create", methods=["POST"])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(CreateAchievementSchema, location="query")
@blp.response(200, AchievementsInputSchema)
def create_achievement(data):
    """
    Create a new achievement
    """
    try:
        new_achievement = Achievements.create_achievements(
            data.get("description"),
            data.get("table"),
            data.get("column"),
            data.get("amount"),
        )

        return new_achievement
    except AchievementExistsException as e:
        response = jsonify({"message": str(e)})
        response.status_code = 422
        return response
    except Exception as e:
        return {"message": str(e)}


@blp.route("users/<int:user_id>", methods=["GET"])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, UserAchievementsListSchema)
def get_users_achievements(user_id: int):
    """
    Get all the users achievements
    """
    user_achievements = Achievements.get_user_achievements(user_id)

    return {"items": user_achievements, "total": len(user_achievements)}
