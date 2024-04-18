import flask
from flask_smorest import Blueprint
from src.models.user import User, UserInputSchema, UserListSchema, UserInputPasswordSchema

api_url = '/user'
api_name = 'User'
api_description = 'User service'

app = flask.Flask(__name__)
app.config["DEBUG"] = True
blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)


@blp.route('/create-user', methods=['POST'])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(UserInputSchema, location='query')
@blp.response(200, UserInputSchema)
def create_user(data):
    """
    Create a new user
    """
    try:
        new_user = User.create_user(
            data.get('name'),
            data.get('last_names'),
            data.get('email'),
            data.get('password'),
            data.get('security_word')
        )
        return new_user
    except Exception as e:
        return {'message': str(e)}


@blp.route('/modify-user', methods=['POST'])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(UserInputSchema, location='query')
@blp.response(200, UserInputSchema)
def modify_user(data):
    """
    Modify an existing user
    """
    try:
        new_user = User.modify_user(
            data.get('name'),
            data.get('last_names'),
            data.get('email'),
            data.get('password'),
            data.get('security_word')
        )
        return new_user
    except Exception as e:
        return {'message': str(e)}


@blp.route('/<int:user_id>', methods=['GET'])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, UserInputSchema)
def get_user_by_id(user_id: int):
    """
    Get a user by his id
    """
    try:
        new_user = User.get_user_by_id(user_id)
        return new_user
    except Exception as e:
        return {'message': str(e)}


@blp.route('/<string:user_email>', methods=['GET'])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, UserInputSchema)
def get_user_by_email(user_email: str):
    """
    Get a user by his email
    """
    try:
        new_user = User.get_user_by_email(user_email)
        return new_user
    except Exception as e:
        return {'message': str(e)}


@blp.route('/<string:user_email>', methods=['GET'])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, UserInputSchema)
def delete_user_by_id(user_id: int):
    """
    Delete a user by his id
    """
    try:
        User.delete_user_by_id(user_id)
    except Exception as e:
        return {'message': str(e)}


@blp.route('/<string:user_email>', methods=['DELETE'])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, UserInputSchema)
def delete_user_by_email(user_email: str):
    """
    Delete a user by his email
    """
    try:
        User.delete_user_by_email(user_email)
    except Exception as e:
        return {'message': str(e)}


@blp.route('/user_list', methods=['GET'])
# @blp.doc(security=[{'JWT': []}])
@blp.response(200, UserListSchema)
def get_all_users():
    """
    Get all the users
    """
    try:
        users = User.get_all_users()

        return {'items': users, 'total': len(users)}
    except Exception as e:
        return {'message': str(e)}


@blp.route('/change-password', methods=['PATCH'])
# @blp.doc(security=[{'JWT': []}])
@blp.arguments(UserInputPasswordSchema, location='query')
@blp.response(200)
def change_user_password(data):
    """
    Get all the users
    """
    try:
        return User.change_user_password(data.get('email'), data.get('new_password'))
    except Exception as e:
        return {'message': str(e)}

