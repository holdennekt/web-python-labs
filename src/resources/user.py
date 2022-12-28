from flask_smorest import Blueprint, abort
from flask.views import MethodView
from src.db import db
from sqlalchemy.exc import IntegrityError

from src.models.user import UserModel
from src.schemas import UserSchema

blp = Blueprint("user", __name__, description="users routes")


@blp.route("/user/<string:user_id>")
class User(MethodView):
  @blp.response(200, UserSchema)
  def get(self, user_id):
    return UserModel.query.get_or_404(user_id)


@blp.route("/user")
class UserList(MethodView):
  @blp.arguments(UserSchema)
  @blp.response(201, UserSchema)
  def post(self, user_data):
    user = UserModel(**user_data)
    try:
      db.session.add(user)
      db.session.commit()
    except IntegrityError:
      abort(400, message="User with such name already exists")
    return user
