from uuid import uuid4
from flask_smorest import Blueprint
from flask.views import MethodView
from src.data import categories

from src.schemas import CategorySchema

blp = Blueprint("category", __name__, description="categories routes")


@blp.route("/category")
class CategoryList(MethodView):
  @blp.response(200, CategorySchema(many=True))
  def get(self):
    return categories

  @blp.arguments(CategorySchema)
  @blp.response(201, CategorySchema)
  def post(self, category_data):
    category = {"id": str(uuid4()), "name": category_data["name"]}
    categories.append(category)
    return category
