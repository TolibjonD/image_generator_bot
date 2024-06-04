from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

photo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖼 Get random photo")]
    ],
    resize_keyboard=True
)