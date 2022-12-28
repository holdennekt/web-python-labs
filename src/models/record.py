from sqlalchemy.sql import functions
from src.db import db

class RecordModel(db.Model):
  __tablename__ = "record"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(
    db.Integer,
    db.ForeignKey("user.id"),
    nullable=False
  )
  category_id = db.Column(
    db.Integer,
    db.ForeignKey("category.id"),
    nullable=False
  )
  sum = db.Column(db.Float(precision=2), nullable=False)
  created_at = db.Column(db.TIMESTAMP, server_default=functions.now())

  user = db.relationship("UserModel", back_populates="records")
  category = db.relationship("CategoryModel", back_populates="records")
