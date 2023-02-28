from flask import request
from flask_restx import Resource, Namespace

from app.container import director_dao
from app.dao.model.director import Director_scheme
from decorator import auth_reguired, admin_reguired

directors_ns = Namespace('directors')

director_scheme = Director_scheme()
directors_scheme = Director_scheme(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_reguired
    def get(self):
        directors = director_dao.get_all()
        return directors_scheme.dump(directors), 200

    @admin_reguired
    def post(self):
        req_json = request.json
        director_dao.create(req_json)

        return "", 201


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_reguired
    def get(self, did: int):
        try:
            director = director_dao.get_one(did)
            return director_scheme.dump(director)
        except Exception:
            return "", 404
    @admin_reguired
    def put(self, did: int):
        req_json = request.json
        req_json["id"] = did
        director_dao.update(req_json)

        return "", 204
    @admin_reguired
    def delete(self, did: int):
        director_dao.delete(did)

        return "", 204
