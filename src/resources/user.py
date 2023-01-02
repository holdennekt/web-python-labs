import os
from flask_jwt_extended import create_access_token, jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from src.db import db
from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256

from src.models.user import UserModel
from src.schemas import UserSchema, LoginSchema, TokenSchema

blp = Blueprint("user", __name__, description="users routes")


@blp.route("/user/<string:user_id>")
class User(MethodView):
  @blp.response(200, UserSchema)
  @jwt_required()
  def get(self, user_id):
    return UserModel.query.get_or_404(user_id)


@blp.route("/register")
class UserList(MethodView):
  @blp.arguments(UserSchema)
  @blp.response(201, TokenSchema)
  def post(self, user_data):
    print("JWT_SECRET_KEY", os.getenv("JWT_SECRET_KEY"))
    user_data["password"] = pbkdf2_sha256.hash(user_data["password"])
    user = UserModel(**user_data)
    try:
      db.session.add(user)
      db.session.commit()
      return { "access_token": create_access_token(identity=user.id) }
    except IntegrityError:
      abort(400, message="User with such name already exists")

@blp.route("/login")
class UserList(MethodView):
  @blp.arguments(LoginSchema)
  @blp.response(201, TokenSchema)
  def post(self, user_data):
    user = UserModel.query.filter(UserModel.name == user_data["name"]).all()
    if user and user[0] and pbkdf2_sha256.verify(user_data["password"], user[0].password):
      return { "access_token": create_access_token(identity=user[0].id) }
    else:
      abort(401, message="Authentication failed")