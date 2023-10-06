import asyncio
import random
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!")

@dp.message_handler(commands=['myinfo'])
async def send_my_info(message: types.Message):
    user_info = f"Ваш id: {message.from_user.id}\n" \
                f"Ваше имя: {message.from_user.first_name}\n" \
                f"Ваш ник: {message.from_user.username}"
    await message.reply(user_info)

@dp.message_handler(commands=['picture'])
async def send_random_picture(message: types.Message):


if __name__ == '__main__':
    from aiogram import executor

    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
