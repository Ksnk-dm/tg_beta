from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from config_reader import config
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Dispatcher, types
from config_reader import config

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
        kb = [
        [types.KeyboardButton(text="Отправить номер телефона 📱", request_contact=True)]]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   
        await message.answer("Пожалуйста, отправьте свой номер телефона.", reply_markup=keyboard)

@dp.message(F.contact)
async def handle_contact(message: types.Message):
    contact = message.contact
    user_name = message.from_user.username
    user_id = message.from_user.id
    await message.answer(f"Спасибо! Ваш номер телефона: {contact.phone_number} {user_name} {user_id}")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")