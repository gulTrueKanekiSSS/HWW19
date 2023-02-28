# main.py

from flask import Flask
from flask_restx import Api
from app.config import Config
from app.data_base import db
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns
from app.views.auth import auth_ns
from app.views.users import user_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()   # применение конфигурации в будущие компоненты

    return application

def configure_app(aplication: Flask):
    db.init_app(aplication)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    db.create_all()
    app.run(debug=True)
