from app.dao.movie import MovieDAO
class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao
    def get_one(self):
        return self.dao.get_movie()
    def get_all(self):
        return self.dao.get_all()
    def create(self, data):
        return self.dao.create(data)