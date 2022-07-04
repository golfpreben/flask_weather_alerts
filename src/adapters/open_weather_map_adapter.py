import requests

from src import settings


class OpenWeatherMapAdapter:
    """ Adapter that encapsulates call to the open weather map service"""
    def __init__(self):
        self.url = settings.URL_OPEN_WEATHER_MAP

    def check_weather_data(self, threshold: int) -> bool:
        """ Checks if temperature is below threshold and
        return True if it is
        """
        response = requests.get(url=self.url )
        response.raise_for_status()
        # Check
        temperature = response.json().get("temperature")
        return temperature < threshold
