from src import app
from flask_smorest import Api
from src.resources.user import blp as UserBlueprint
from src.resources.category import blp as CategoryBlueprint
from src.resources.record import blp as RecordBlueprint

app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app, spec_kwargs={
  "title":"Lab 2",
  "version":"v1",
  "openapi_version": "3.0.3"
})

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)
