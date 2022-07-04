from flask import Flask, Blueprint
from flask_migrate import Migrate

from src import settings
from src.controllers.restx_config import api
from src.controllers.alert_controller import ns as alert_namespace


blueprint = Blueprint(settings.FLASK_BLUEPRINT_URL, __name__,
                      url_prefix="/" + settings.FLASK_BLUEPRINT_URL)

api.init_app(blueprint)

# Adding namespaces to blueprint
api.add_namespace(alert_namespace)

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

    from src.models.base_model import db
    db.init_app(app)

    # Setup migrations
    migrate.init_app(app=app, db=db, directory="migrations")
    app.register_blueprint(blueprint)

    return app
