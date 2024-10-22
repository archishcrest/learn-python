from flask import request
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from models import User
from schemas import UserSchema
from db import db
from datetime import timedelta

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'])
    user.set_password(data['password'])
    user.save()
    return {"message": "User registered successfully"}, 201

@blp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects(username=data['username']).first()
    if user and user.check_password(data['password']):

        # RevokedToken.query.filter_by(user_id=user.id).all().delete()

        # if jti:
        #     revoked_token = RevokedToken(jti=jti)
        #     revoked_token.save()

        access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1), fresh=True)
        return {"access_token": access_token}, 200
    return {"message": "Invalid credentials"}, 401
