from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from src.db import db
from sqlalchemy.exc import IntegrityError

from src.models.record import RecordModel
from src.models.user import UserModel
from src.schemas import RecordSchema, RecordQuerySchema

blp = Blueprint("record", __name__, description="records routes")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
  @blp.response(200, RecordSchema)
  def get(self, record_id):
    return RecordModel.query.get_or_404(record_id)


@blp.route("/record")
class RecordList(MethodView):
  @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
  @blp.response(200, RecordSchema(many=True))
  @jwt_required()
  def get(self, user_id, **kwargs):
    category_id = kwargs.get('category_id', None)
    query = RecordModel.query.filter(RecordModel.user_id == user_id)
    if category_id:
      query = query.filter(RecordModel.category_id == category_id)
    return query.all()

  @blp.arguments(RecordSchema)
  @blp.response(201, RecordSchema)
  @jwt_required()
  def post(self, record_data):
    currency_id = record_data.get('currency_id', None)
    if not currency_id:
      user_id = record_data.get('user_id')
      user = UserModel.query.get_or_404(user_id)
      record_data["currency_id"] = user.default_currency_id
    record = RecordModel(**record_data)
    try:
      db.session.add(record)
      db.session.commit()
    except IntegrityError:
      abort(400, message="Wrong input")
    return record
