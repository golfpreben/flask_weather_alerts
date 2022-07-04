from typing import List

from flask_restx import Namespace, Resource

from src.controllers.alert_restx_marshall import alert_marshall
from src.controllers.restx_config import api
from src.models.alert_model import AlertModel
from src.services.alert_srv import AlertService

ns = Namespace("alerts", description="Rest API for alerts", validate=True)

alert_service = AlertService()

@ns.route('/')
class AlertsController(Resource):

    """ Shows a list of alerts """
    @ns.marshal_list_with(alert_marshall)
    def get(self) -> List[AlertModel]:
        return alert_service.get_alerts()

    """ Creates an alert """
    @ns.expect(alert_marshall)
    @ns.marshal_with(alert_marshall)
    def post(self) -> AlertModel:
        payload_dict = api.payload
        alert_model_obj: AlertModel = AlertModel()
        alert_model_obj.temperature_below_threshold_celsius = payload_dict.get('temperature_below_threshold_celsius')
        alert_model_obj.alert_destination = payload_dict.get('alert_destination')

        return alert_service.create_alert(alert_model_obj), 201


@ns.route('/check/<int:id>')
@ns.param('id', 'id of the alert to check')
class CheckAlertsController(Resource):
    """ Checks an alert with the specified id """
    @ns.marshal_list_with(alert_marshall)
    def get(self, id) -> AlertModel:
        # TODO: fetch the alert with the id, check the threshold, save it and return it.
        return 200
