import datetime


def weather_answer(weather_data: dict) -> str:
    return f"{weather_data['location']}. {datetime.date.today()}\n" \
           f"Temperature is {weather_data['temp']}" \
           f" and feels like {weather_data['feels_like']}.\n" \
           f"It's {weather_data['desc']}.\n" \
           f"Sunrise time: {weather_data['sunrise']}.\n" \
           f"Sunset time: {weather_data['sunset']}.\n" \
           f"Wind speed : {weather_data['wind_speed']}.\n" \
           f"Wind direction: {weather_data['wind_direction']}."
