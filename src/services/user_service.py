from flask_smorest import Blueprint

api_url = '/user'
api_name = 'User'
api_description = 'User service'

blp = Blueprint(
    name=api_name,
    description=api_description,
    url_prefix=api_url,
    import_name=__name__,
)

@blp.route('', methods=['GET'])
def get_user():
    return True
