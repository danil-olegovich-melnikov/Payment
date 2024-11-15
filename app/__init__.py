from flask import Flask
from .models import db
from flask_migrate import Migrate
from config import Config
from app.urls import main as main_blueprint


migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_blueprint)

    return app