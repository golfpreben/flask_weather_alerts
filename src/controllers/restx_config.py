from flask_restx import Api

api = Api(version='1.0', title='weather alert API',
    description='An API to setup weather alerts', security=None)
