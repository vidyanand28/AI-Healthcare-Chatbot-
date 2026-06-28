from flask import Flask
from config import BASE_DIR


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
    )

    from .predictor import Predictor
    from .routes import register_routes

    predictor = Predictor()
    register_routes(app, predictor)
    return app
