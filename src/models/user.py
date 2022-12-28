from src.db import db

class UserModel(db.Model):
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), unique=True, nullable=False)

  records = db.relationship(
    "RecordModel",
    back_populates="user",
    lazy="dynamic",
  )
