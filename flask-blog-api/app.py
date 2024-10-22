import os
from flask import Flask, request
from flask_smorest import Api
from db import db
import models
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from resources.blog import blp as BlogBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url=None):

	load_dotenv()

	app = Flask(__name__)
	app.config["API_TITLE"] = "Blogs REST API"
	app.config["API_VERSION"] = "v1"
	app.config['OPENAPI_VERSION'] = '3.0.2'
	app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
	app.config['CASSANDRA_KEYSPACE'] = "blog_keyspace"
	app.config['CQLENGINE_DEFAULT_CONNECTION '] = "blog_db"

	db.init_app(app)

	with app.app_context():
		db.sync_db()

	api = Api(app)

	app.config["JWT_SECRET_KEY"] = "dsfsdfret54tfr#fert51111!!@@@@@erff98f39f89i9f"
	jwt = JWTManager(app)

	# @jwt.token_in_blocklist_loader
	# def check_if_token_revoked(jwt_header, jwt_payload):
	# 	jti = jwt_payload['jti']  # Get the JWT ID from the payload
	# 	return RevokedToken.query.filter_by(jti=jti).first() is not None

	# @jwt.token_in_blocklist_loader
	# def check_if_token_revoked(jwt_header, jwt_payload):
	# 	jti = jwt_payload['jti']
	# 	return RevokedToken.query.filter_by(jti=jti).first() is not None

	@jwt.expired_token_loader
	def expired_token_callback(jwt_header, jwt_payload):
	    return (
	        jsonify({"message": "The token has expired.", "error": "token_expired"}),
	        401,
	    )

	@jwt.invalid_token_loader
	def invalid_token_callback(error):
	    return (
	        jsonify(
	            {"message": "Signature verification failed.", "error": "invalid_token"}
	        ),
	        401,
	    )

	@jwt.unauthorized_loader
	def missing_token_callback(error):
	    return (
	        jsonify(
	            {
	                "description": "Request does not contain an access token.",
	                "error": "authorization_required",
	            }
	        ),
	        401,
	    )

	@jwt.revoked_token_loader
	def revoked_token_response(callback):
		return (
	        jsonify(
	            {
	                "description": "The token has been revoked.",
	                "error": "authorization_required",
	            }
	        ),
	        401,
	    )

	api.register_blueprint(BlogBlueprint)
	api.register_blueprint(UserBlueprint)

	return app