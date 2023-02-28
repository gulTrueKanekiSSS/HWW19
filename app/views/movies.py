from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_dao
from app.dao.model.movie import Movie_scheme, Movie
from app.data_base import db
from decorator import auth_reguired, admin_reguired

movies_ns = Namespace('movies')

movie_schema = Movie_scheme()
movies_schema = Movie_scheme(many=True)

@movies_ns.route('/')
class MoviesView(Resource):
    @auth_reguired
    def get(self):
        director_id = request.args.get("director_id")

        genre_id = request.args.get("genre_id")

        movie_year = request.args.get("year")

        if genre_id and director_id:
            try:
                movies = db.session.query(Movie).filter(Movie.genre_id == genre_id, Movie.director_id == director_id).all()
                return movies_schema.dump(movies)
            except Exception:
                return "", 404
        elif director_id:
            try:
                movies = db.session.query(Movie).filter(Movie.director_id == director_id).all()
                return movies_schema.dump(movies)
            except Exception:
                return "", 404

        elif genre_id:
            try:
                movies = db.session.query(Movie).filter(Movie.genre_id == genre_id).all()
                return movies_schema.dump(movies)
            except Exception:
                return "These movies don't exist", 404
        elif movie_year:
            try:
                movies = db.session.query(Movie).filter(Movie.year == movie_year).all()
                return movies_schema.dump(movies)
            except Exception:
                return "These movies don't exist", 404
        else:
            all_movie = movie_dao.get_all()
            return movies_schema.dump(all_movie), 200
    @admin_reguired
    def post(self):
        req_json = request.json
        movie_dao.create(req_json)

        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_reguired
    def get(self, mid: int):
        try:
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception:
            return "", 404