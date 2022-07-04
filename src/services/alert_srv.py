from typing import List

from flask_restx import abort

from src.data_access_layer.alert_dal import AlertDAL
from src.models.alert_model import AlertModel


class AlertService:
    """ Service which handles business logic related to alerts """

    class AlertDestinations:
        """
        Possible alert destinations
        """
        EMAIL = "EMAIL"
        SMS = "SMS"

    AlertDestinationsList = [AlertDestinations.EMAIL, AlertDestinations.SMS]

    def __init__(self):
        self.alert_dal = AlertDAL()

    def validate_alert(self, alert_model: AlertModel):
        if abs(alert_model.temperature_below_threshold_celsius) > 80:
            abort(400, "Threshold exceed max allowed value")
        if alert_model.alert_destination not in AlertService.AlertDestinationsList:
            abort(400, "Alert destination is invalid")

    def get_alerts(self) -> List[AlertModel]:
        """ Calls alert DAL for list of alerts """
        return self.alert_dal.get_alerts()

    def create_alert(self, alert_model_obj: AlertModel) -> AlertModel:
        """ Calls alert DAL to create alert """
        self.validate_alert(alert_model_obj)
        return self.alert_dal.create_alert(alert_model_obj)
