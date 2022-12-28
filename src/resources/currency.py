from flask_smorest import Blueprint, abort
from flask.views import MethodView
from src.db import db
from sqlalchemy.exc import IntegrityError

from src.models.currency import CurrencyModel
from src.schemas import CurrencySchema

blp = Blueprint("currency", __name__, description="currencies routes")


@blp.route("/currency/<string:currency_id>")
class Currency(MethodView):
  @blp.response(200, CurrencySchema)
  def get(self, currency_id):
    return CurrencyModel.query.get_or_404(currency_id)


@blp.route("/currency")
class CurrencyList(MethodView):
  @blp.response(200, CurrencySchema(many=True))
  def get(self):
    return CurrencyModel.query.all()

  @blp.arguments(CurrencySchema)
  @blp.response(201, CurrencySchema)
  def post(self, currency_data):
    currency = CurrencyModel(**currency_data)
    try:
      db.session.add(currency)
      db.session.commit()
    except IntegrityError:
      abort(400, message="currency with such name already exists")
    return currency
