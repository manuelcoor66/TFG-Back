from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from src.models.user import db
from src.services import user_service, league_service, enrolments_service

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)

# Configurar la base de datos
app.config["API_TITLE"] = "TFG API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "apidocs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://root:1a2b3c4d5e!$@localhost:5432/tfg"
)

# Inicializar la instancia de SQLAlchemy
db.init_app(app)

# Crear una instancia de Api con Flask-Smorest
api = Api(app)

# Registrar el Blueprint del servicio de usuario
api.register_blueprint(user_service.blp)
api.register_blueprint(league_service.blp)
api.register_blueprint(enrolments_service.blp)

if __name__ == "__main__":
    app.run(debug=True)
