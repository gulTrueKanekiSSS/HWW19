from marshmallow import Schema, fields

from app.data_base import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
class Director_scheme(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()