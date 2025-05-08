from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sura"), KeyboardButton(text="Oyat")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Kerakli bo‘limni tanlang..."
)
