import logging
from typing import List

from flask_restx import abort

from src.adapters.open_weather_map_adapter import OpenWeatherMapAdapter
from src.data_access_layer.alert_dal import AlertDAL
from src.models.alert_model import AlertModel

log = logging.getLogger(__name__)


class AlertService:
    """ Service which handles business logic related to alerts """

    class AlertDestinations:
        """
        Possible alert destinations
        """
        EMAIL = "EMAIL"
        SMS = "SMS"

    AlertDestinationsList = [AlertDestinations.EMAIL, AlertDestinations.SMS]

    def __init__(self, alert_dal: AlertDAL = None,
                 open_weather_map_adapter: OpenWeatherMapAdapter = None):
        self.alert_dal = alert_dal or AlertDAL()
        self.open_weather_map_adapter = open_weather_map_adapter or OpenWeatherMapAdapter()

    def _validate_alert(self, alert_model: AlertModel):
        if abs(alert_model.temperature_below_threshold_celsius) > 80:
            abort(400, "Threshold exceed max allowed value")
        if alert_model.alert_destination not in AlertService.AlertDestinationsList:
            abort(400, "Alert destination is invalid")

    def _check_alert(self, alert_model_obj: AlertModel) -> bool:
        """ Calls adapters to check on threshold"""
        threshold_exceeded = None
        try:
            threshold_exceeded = self.open_weather_map_adapter.check_weather_data(alert_model_obj.
                                                                                  temperature_below_threshold_celsius)
        except Exception as e:
            log.error("Failed to get weather data")
        return threshold_exceeded

    def get_alerts(self) -> List[AlertModel]:
        """ Calls alert DAL for list of alerts """
        return self.alert_dal.get_alerts()

    def create_alert(self, alert_model_obj: AlertModel) -> AlertModel:
        """ Validates, checks threshold and calls alert DAL to create alert """
        self._validate_alert(alert_model_obj)
        threshold_exceeded = self._check_alert(alert_model_obj)
        alert_model_obj.threshold_exceeded = threshold_exceeded
        response = self.alert_dal.create_alert(alert_model_obj)

        return response
