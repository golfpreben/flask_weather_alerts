from decouple import config

FLASK_HOST = config("FLASK_HOST", default="0.0.0.0")
FLASK_BLUEPRINT_URL = config("FLASK_BLUEPRINT_URL", default="api")