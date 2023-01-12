import json
from enum import IntEnum
from urllib.request import urlopen
from dataclasses import dataclass
from datetime import datetime
import config

class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315
class Weather:

    def __init__(self, coordinates):
        self.data = self.get_weather(coordinates)


    def get_weather(self, coordinates):
        # Request to API
        openweather_response = self._get_openweather_response(latitude=coordinates.latitude, longitude=coordinates.longitude)
        weather_data = self._parse_openweather_response_data(response_data=openweather_response)
        # todo returm a data from _parse_openweather_response_data
        return weather_data
    @staticmethod
    def _get_openweather_response(latitude, longitude):
        url = config.CURRENT_WEATHER_API_CALL.format(latitude=latitude, longitude=longitude)
        return urlopen(url).read()


    @staticmethod
    def _parse_sun_time(weather_data: dict, suntime: str):
        return datetime.fromtimestamp(weather_data['sys'][suntime]).strftime('%H:%M')

    @staticmethod
    def _parse_temperature(weather_data: dict):
        return weather_data['main']['temp']

    @staticmethod
    def _parse_temperature_feel(weather_data: dict):
        return weather_data['main']['feels_like']

    @staticmethod
    def _parse_weather_description(weather_data: dict):
        return weather_data['weather'][0]['description']

    @staticmethod
    def _parse_location(weather_data: dict):
        return weather_data['name']
    @staticmethod
    def _parse_wind_speed(weather_data: dict):
        return weather_data['wind']['speed']

    @staticmethod
    def _parse_wind_direction(weather_data: dict):
        wind_degrees = weather_data['wind']['deg']
        wind_degrees = round(wind_degrees/ 45) * 45
        if wind_degrees == 360:
            wind_degrees = 0
        return WindDirection(wind_degrees).name

    def _parse_openweather_response_data(self, response_data):
        weather_data = json.loads(response_data)
        location = weather_data['name']
        temp = self._parse_temperature(weather_data)
        feels_like = self._parse_temperature_feel(weather_data)
        description = self._parse_weather_description(weather_data)
        sunrise = self._parse_sun_time(weather_data, 'sunrise')
        sunset = self._parse_sun_time(weather_data, 'sunset')
        wind_speed = self._parse_wind_speed(weather_data)
        wind_direction = self._parse_wind_direction(weather_data)
        weather_data = {'location': location,
                        'temp': temp,
                        'feels_like': feels_like,
                        'desc': description,
                        'sunrise': sunrise,
                        'sunset': sunset,
                        'wind_speed': wind_speed,
                        'wind_direction': wind_direction
                        }
        return weather_data