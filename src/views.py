from src import app
from flask_smorest import Api

from src.resources.user import blp as UserBlueprint
from src.resources.category import blp as CategoryBlueprint
from src.resources.record import blp as RecordBlueprint
from src.resources.currency import blp as CurrencyBlueprint
from src.db import db

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Lab 2"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

api = Api(app)

with app.app_context():
  db.create_all()

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)
api.register_blueprint(CurrencyBlueprint)
