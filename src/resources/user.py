from uuid import uuid4
from flask_smorest import Blueprint
from flask.views import MethodView
from src.data import users

from src.schemas import UserSchema

blp = Blueprint("user", __name__, description="users routes")


@blp.route("/user/<string:user_id>")
class User(MethodView):
  @blp.response(200, UserSchema)
  def get(self, user_id):
    user = list(
        filter(
            lambda record: (record["id"] == user_id),
            users
        )
    )
    return user


@blp.route("/user")
class UserList(MethodView):
  @blp.arguments(UserSchema)
  @blp.response(201, UserSchema)
  def post(self, user_data):
    user = {"id": str(uuid4()), "name": user_data["name"]}
    users.append(user)
    return user
