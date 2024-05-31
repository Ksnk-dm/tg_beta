import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from config_reader import config
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers import dp

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())

async def main():
    await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())