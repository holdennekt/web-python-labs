from uuid import uuid4
from flask_smorest import Blueprint
from flask.views import MethodView
from src.data import users

from src.schemas import UserSchema

blp = Blueprint("user", __name__, description="users routes")


@blp.route("/user/<string:user_id>")
class User(MethodView):
  def get(self, user_id):
    return


@blp.route("/user")
class UserList(MethodView):
  @blp.arguments(UserSchema)
  def post(self, user_data):
    user = {"id": str(uuid4()), "name": user_data["name"]}
    users.append(user)
    return user
