from flask import Flask

app = Flask(__name__)
# CORS(app)
app.config["API_TITLE"] = "TFG API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "apidocs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["DEBUG"] = True
# weather_api = Api(app)

"""
Blueprint definition
"""
# weather_api.register_blueprint(basic_endpoints)


if __name__ == "__main__":
    app.run(debug=True)
