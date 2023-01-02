from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from src.db import db
from sqlalchemy.exc import IntegrityError

from src.models.category import CategoryModel
from src.schemas import CategorySchema

blp = Blueprint("category", __name__, description="categories routes")


@blp.route("/category/<string:category_id>")
class Category(MethodView):
  @blp.response(200, CategorySchema)
  def get(self, category_id):
    return CategoryModel.query.get_or_404(category_id)


@blp.route("/category")
class CategoryList(MethodView):
  @blp.response(200, CategorySchema(many=True))
  def get(self):
    return CategoryModel.query.all()

  @blp.arguments(CategorySchema)
  @blp.response(201, CategorySchema)
  @jwt_required()
  def post(self, category_data):
    category = CategoryModel(**category_data)
    try:
      db.session.add(category)
      db.session.commit()
    except IntegrityError:
      abort(400, message="Category with such name already exists")
    return category
