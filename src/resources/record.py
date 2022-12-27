from datetime import datetime
from uuid import uuid4
from flask_smorest import Blueprint
from flask.views import MethodView
from src.data import records

from src.schemas import RecordSchema, RecordQuerySchema

blp = Blueprint("record", __name__, description="records routes")


@blp.route("/record")
class RecordList(MethodView):
  @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
  @blp.response(200, RecordSchema(many=True))
  def get(self, user_id, **kwargs):
    category_id = kwargs.get('category_id', None)
    user_records = list(
        filter(
            lambda r: (
                r["user_id"] == user_id and
                (True if category_id is None else r["category_id"] == category_id)
            ),
            records
        )
    )
    return user_records

  @blp.arguments(RecordSchema)
  @blp.response(201, RecordSchema)
  def post(self, record_data):
    record = {
        "id": str(uuid4()),
        "user_id": record_data["user_id"],
        "category_id": record_data["category_id"],
        "created_at": str(datetime.now()),
        "sum": record_data["sum"]
    }
    records.append(record)
    return record


@blp.route("/record/<string:record_id>")
class Record(MethodView):
  @blp.response(200, RecordSchema)
  def get(self, record_id):
    record = list(
        filter(
            lambda record: (record["id"] == record_id),
            records
        )
    )
    return record
