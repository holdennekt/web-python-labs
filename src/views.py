from src import app
from flask import jsonify, request
from uuid import uuid4
from datetime import datetime
from src.data import users, categories, records

@app.route("/users", methods=["POST"])
def create_user():
  user = { "id": str(uuid4()), "name": request.json["name"] }
  users.append(user)
  return jsonify(user)

@app.route("/categories")
def get_categories():
  return jsonify(categories)

@app.route("/categories", methods=["POST"])
def create_category():
  category = { "id": str(uuid4()), "name": request.json["name"] }
  categories.append(category)
  return jsonify(category)

@app.route("/records")
def get_user_recors():
  user_id = request.args.get("user_id")
  category_id = request.args.get("category_id")
  users_records = list(filter(lambda r: r["user_id"] == user_id and (True if category_id is None else r["category_id"] == category_id), records))
  return jsonify(users_records)

@app.route("/records", methods=["POST"])
def create_record():
  record = {
    "id": str(uuid4()),
    "user_id": request.json["user_id"],
    "category_id": request.json["category_id"],
    "created_at": str(datetime.now()),
    "sum": request.json["sum"]
  }
  records.append(record)
  return jsonify(record)