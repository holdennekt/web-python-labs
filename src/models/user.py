from src.db import db

class UserModel(db.Model):
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  default_currency_id = db.Column(
    db.Integer,
    db.ForeignKey("currency.id"),
    nullable=False,
  )

  default_currency = db.relationship(
    "CurrencyModel",
    back_populates="users",
    lazy="joined",
  )
  records = db.relationship(
    "RecordModel",
    back_populates="user",
    lazy="dynamic",
  )
