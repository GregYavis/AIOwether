from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

data = CallbackData('content', 'action', 'button_name')


def basic_keyboard():
    markup = ReplyKeyboardMarkup(row_width=1)
    #weather = InlineKeyboardButton('Weather', callback_data=data.new(action='weather', button_name='-'))
    #markup.add(weather)
    coordinates = KeyboardButton('Get the weather', callback_data='coordinates', request_location=True)
    markup.add(coordinates)
    return markup


def request_weather_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    weather = InlineKeyboardButton('Weather', callback_data=data.new(action='weather', button_name='-'))
    markup.add(weather)
    return markup
