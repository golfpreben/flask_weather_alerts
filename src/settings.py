from decouple import config

FLASK_HOST = config('FLASK_HOST', default='0.0.0.0')
FLASK_BLUEPRINT_URL = config('FLASK_BLUEPRINT_URL', default='api')
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)