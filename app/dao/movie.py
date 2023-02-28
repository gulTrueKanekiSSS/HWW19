from flask import request

from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session
    def get_movie(self):
        gid = request.args.get("genre_id")
        did = request.args.get("director_id")
        if gid and did:
            return self.session.query(Movie).filter(Movie.genre_id == gid, Movie.director_id == did).all()
        elif did:
            return self.session.query(Movie).filter(Movie.director_id == did).all()
        elif gid:
            return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie
