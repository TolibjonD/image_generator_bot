from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.photo import photo
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n Tasodifiy rasmlarni olish uchun pastdagi tugmani bosing !...", reply_markup=photo)
