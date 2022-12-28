from flask_smorest import Blueprint
from flask.views import MethodView
from src.db import db
from sqlalchemy.exc import IntegrityError

from src.models.record import RecordModel
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
  def get(self, user_id, **kwargs):
    category_id = kwargs.get('category_id', None)
    query = RecordModel.query.filter(user_id == user_id)
    if category_id:
      query = query.filter(category_id == category_id)
    return query.all()

  @blp.arguments(RecordSchema)
  @blp.response(201, RecordSchema)
  def post(self, record_data):
    record = RecordModel(**record_data)
    db.session.add(record)
    db.session.commit()
    return record
