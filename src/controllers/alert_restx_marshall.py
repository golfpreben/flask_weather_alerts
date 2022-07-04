from flask_restx import fields

from src.controllers.restx_config import api
from src.services.alert_srv import AlertService

alert_fields = {
    'id': fields.Integer(readOnly=True, description='id of alert', example='2'),
    'created_ts': fields.String(readOnly=True, description='creation time'),
    'updated_ts': fields.String(readOnly=True, description='creation time'),
    'temperature_below_threshold_celsius': fields.Integer(
        required=True,
        description='A temperature below this threshold will trigger an alert',
        example='13'),
    'alert_destination': fields.String(required=True,
                                       description=f'Alert destination should be one of these: '
                                                   f'{AlertService.AlertDestinationsList}',
                                       example=f'{AlertService.AlertDestinations.EMAIL}')
}

alert_marshall = api.model("alert", alert_fields)