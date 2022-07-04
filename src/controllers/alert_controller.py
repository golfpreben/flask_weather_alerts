from flask_restx import Namespace, Resource

ns = Namespace("alerts", description="Rest API for alerts", validate=True)

@ns.route('/')
class AlertsController(Resource):
    ''' Shows a list alerts '''

    def get(self):
        return 200