import os
from flask import Flask, request, jsonify
from db import init_app
from flask_smorest import Api
from dotenv import load_dotenv

from resources.face import blp as FaceBlueprint

def create_app():

    app = Flask(__name__)    
    
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URI_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"

    api = Api(app)
    init_app(app)

    # Add resources
    api.register_blueprint(FaceBlueprint)

    return app
