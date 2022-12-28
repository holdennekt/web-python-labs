from src.db import db

class CurrencyModel(db.Model):
  __tablename__ = "currency"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), unique=True, nullable=False)
  
  users = db.relationship(
    "UserModel",
    back_populates="default_currency",
    lazy="dynamic",
  )
