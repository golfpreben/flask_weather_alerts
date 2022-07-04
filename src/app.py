from flask import Flask, Blueprint
from src import settings
from src.controllers.restx_config import api
from src.controllers.alert_controller import ns as alert_namespace


blueprint = Blueprint(settings.FLASK_BLUEPRINT_URL, __name__,
                      url_prefix="/" + settings.FLASK_BLUEPRINT_URL)

api.init_app(blueprint)

# Adding namespaces to blueprint
api.add_namespace(alert_namespace)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

#    from yourapplication.model import db
#    db.init_app(app)

    app.register_blueprint(blueprint)

    return app
