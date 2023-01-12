import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData

from config import TOKEN

from inline_keyboard import basic_keyboard, request_weather_keyboard
from weather_bot.message_templates import weather_answer
from weather_bot.weather_api import Weather

button_action = CallbackData('content', 'action', 'button_name')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome_message(message: types.Message):
    """
    Send welcome message to user
    """
    await message.answer(text='Chose wisely', reply_markup=basic_keyboard())


@dp.message_handler(content_types=["location"])
async def handle_location(message: types.Message):
    coords = message.location
    weather = Weather(coords)
    await message.answer(text=weather_answer(weather.data),
                         reply_markup=request_weather_keyboard())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
