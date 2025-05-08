from aiogram import html, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from help import get_sura, get_oyat
from keyboards import main_menu
from states import user_state
from aiogram import Dispatcher

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer("Quyidagi bo‘limlardan birini tanlang:", reply_markup=main_menu)

@dp.message(F.text == "Sura")
async def sura_button_handler(message: Message):
    user_state[message.from_user.id] = "awaiting_sura_number"
    await message.answer("Iltimos, sura raqamini yuboring (1–114):")

@dp.message(F.text == "Oyat")
async def oyat_button_handler(message: Message):
    user_state[message.from_user.id] = "awaiting_oyat"
    await message.answer("Iltimos, oyat raqamini yuboring (1 255) shaklida :")

@dp.message(F.text.regexp(r"^\d+(\s+\d+)?$"))
async def handle_numbers(message: Message):
    user_id = message.from_user.id
    state = user_state.get(user_id)

    if state == "awaiting_sura_number":
        sura_number = int(message.text)
        if 1 <= sura_number <= 114:
            data = get_sura(sura_number)
            if "text" in data:
                await message.answer(f"{sura_number}-sura:\n\n{data['text']}")
            else:
                await message.answer("Ma'lumot topilmadi.")
        else:
            await message.answer("Sura raqami 1 dan 114 gacha bo‘lishi kerak.")
        user_state.pop(user_id, None)

    elif state == "awaiting_oyat":
        parts = message.text.strip().split()
        if len(parts) == 2:
            sura, oyat = map(int, parts)
            if 1 <= sura <= 114:
                data = get_oyat(sura, oyat)
                if "text" in data:
                    await message.answer(f"{sura}-sura, {oyat}-oyat:\n\n{data['text']}")
                else:
                    await message.answer("Oyat topilmadi.")
            else:
                await message.answer("Sura raqami 1 dan 114 gacha bo‘lishi kerak.")
        else:
            await message.answer("Iltimos, oyatni `sura oyat` shaklida yuboring.")
        user_state.pop(user_id, None)
