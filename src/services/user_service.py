import flask
from flask_smorest import Blueprint
from src.models.user import User, UserInputSchema

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
    new_user = User.create_user(
        data.get('name'),
        data.get('last_names'),
        data.get('email'),
        data.get('password'),
        data.get('security_word')
    )
    return new_user


