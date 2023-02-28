from marshmallow import fields, Schema

from create_data import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}                #####################
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)


class User_scheme(Schema):
    id = fields.Int
    username = fields.Str
    password = fields.Str
    role = fields.Str




