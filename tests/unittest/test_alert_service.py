import unittest
from unittest.mock import Mock, create_autospec, patch

from src.adapters.open_weather_map_adapter import OpenWeatherMapAdapter
from src.data_access_layer.alert_dal import AlertDAL
from src.models.alert_model import AlertModel
from src.services.alert_srv import AlertService


class TestAlertService(unittest.TestCase):

    def _create_service_mock(self, threshold: int, alert_dest: str):
        alert_dal_mock = create_autospec(AlertDAL)

        open_weather_map_adapter_mock = create_autospec(OpenWeatherMapAdapter)
        open_weather_map_adapter_mock.check_weather_data.return_value = True
        alert_service = AlertService(alert_dal=alert_dal_mock,
                                     open_weather_map_adapter=open_weather_map_adapter_mock)

        alert_model_obj: AlertModel = AlertModel()
        alert_model_obj.temperature_below_threshold_celsius = threshold
        alert_model_obj.alert_destination = alert_dest

        return alert_dal_mock, alert_service, alert_model_obj

    def test_create_alert_success(self):
        # Arrange
        THRESHOLD = 10
        ALERT_DESTINATION = AlertService.AlertDestinations.EMAIL

        alert_dal_mock, alert_service, alert_model_obj = self._create_service_mock(THRESHOLD,
                                                                                   ALERT_DESTINATION)

        # Test
        alert_service.create_alert(alert_model_obj)

        # Validate
        alert_dal_mock.create_alert(alert_model_obj).called_once()

    def test_create_alert_wrong_alert_destination(self):
        # Arrange
        THRESHOLD = 10
        ALERT_DESTINATION = "random_text"

        alert_dal_mock, alert_service, alert_model_obj = self._create_service_mock(THRESHOLD,
                                                                                   ALERT_DESTINATION)

        # Test
        with self.assertRaises(Exception) as e:
            alert_service.create_alert(alert_model_obj)

        # Validate
        self.assertTrue(e.exception.code == 400)
        self.assertTrue(e.exception.data.get('message') == 'Alert destination is invalid')


    def test_create_alert_wrong_threshold(self):
        # Arrange
        THRESHOLD = 100
        ALERT_DESTINATION = AlertService.AlertDestinations.EMAIL

        alert_dal_mock, alert_service, alert_model_obj = self._create_service_mock(THRESHOLD,
                                                                                   ALERT_DESTINATION)

        # Test
        with self.assertRaises(Exception) as e:
            alert_service.create_alert(alert_model_obj)

        # Validate
        self.assertTrue(e.exception.code == 400)
        self.assertTrue(e.exception.data.get('message') == 'Threshold exceed max allowed value')
