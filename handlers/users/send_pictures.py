from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from image_generator import image_generator
from keyboards.inline.category import inline_markup, back_btn
from keyboards.inline.callback_query import category_callback

@dp.message_handler(Text("🖼 Get random photo"))
async def send_picture(msg: types.Message):
    txt = "Qaysi mavzudagi rasmni olmoqchisz ?\nPastdan kerakli mavzuni tanglang !"
    await msg.answer(text=txt, reply_markup=inline_markup)
    
@dp.callback_query_handler(category_callback.filter(item_name="art"))
async def send_art_pictures(call: types.CallbackQuery):
    try:
        category = "art"
        data = image_generator(category)
        caption = f"ℹ️ {data['descr']}\n\n"
        caption += f"❤️ {data['likes']}"
        await call.message.delete()
        await call.message.answer_photo(photo=data['image'], caption=caption, reply_markup=back_btn)
        await call.answer(cache_time=60)
    except:
        await call.message.answer("Bu kategoriya bo'yicha rasm topilmadi ! Yana tanlab ko'ring topishga harakat qilaman yoki \n\nPastdan bo'limni tanlang !", reply_markup=inline_markup)
        await call.answer(cache_time=60)
@dp.callback_query_handler(category_callback.filter(item_name="vehicle"))
async def send_art_pictures(call: types.CallbackQuery):
    try:
        category = "vehicle"
        data = image_generator(category)
        caption = f"ℹ️ {data['descr']}\n\n"
        caption += f"❤️ {data['likes']}"
        await call.message.delete()
        await call.message.answer_photo(photo=data['image'], caption=caption, reply_markup=back_btn)
        await call.answer(cache_time=60)
    except:
        await call.message.answer("Bu kategoriya bo'yicha rasm topilmadi ! Yana tanlab ko'ring topishga harakat qilaman yoki \n\nPastdan bo'limni tanlang !", reply_markup=inline_markup)
        await call.answer(cache_time=60)
@dp.callback_query_handler(category_callback.filter(item_name="travel"))
async def send_art_pictures(call: types.CallbackQuery):
    try:
        category = "travel"
        data = image_generator(category)
        caption = f"ℹ️ {data['descr']}\n\n"
        caption += f"❤️ {data['likes']}"
        await call.message.delete()
        await call.message.answer_photo(photo=data['image'], caption=caption, reply_markup=back_btn)
        await call.answer(cache_time=60)
    except:
        await call.message.answer("Bu kategoriya bo'yicha rasm topilmadi ! Yana tanlab ko'ring topishga harakat qilaman yoki \n\nPastdan bo'limni tanlang !", reply_markup=inline_markup)
        await call.answer(cache_time=60)
@dp.callback_query_handler(category_callback.filter(item_name="work"))
async def send_art_pictures(call: types.CallbackQuery):
    try:
        category = "film"
        data = image_generator(category)
        caption = f"ℹ️ {data['descr']}\n\n"
        caption += f"❤️ {data['likes']}"
        await call.message.delete()
        await call.message.answer_photo(photo=data['image'], caption=caption, reply_markup=back_btn)
        await call.answer(cache_time=60)
    except:
        await call.message.answer("Bu kategoriya bo'yicha rasm topilmadi ! Yana tanlab ko'ring topishga harakat qilaman yoki \n\nPastdan bo'limni tanlang !", reply_markup=inline_markup)
        await call.answer(cache_time=60)
@dp.callback_query_handler(category_callback.filter(item_name="current_events"))
async def send_art_pictures(call: types.CallbackQuery):
    try:
        category = "current events"
        data = image_generator(category)
        caption = f"ℹ️ {data['descr']}\n\n"
        caption += f"❤️ {data['likes']}"
        await call.message.delete()
        await call.message.answer_photo(photo=data['image'], caption=caption, reply_markup=back_btn)
        await call.answer(cache_time=60)
    except:
        await call.message.answer("Bu kategoriya bo'yicha rasm topilmadi ! Yana tanlab ko'ring topishga harakat qilaman yoki \n\nPastdan bo'limni tanlang !", reply_markup=inline_markup)
        await call.answer(cache_time=60)
@dp.callback_query_handler(category_callback.filter(item_name="nature"))
async def send_art_pictures(call: types.CallbackQuery):
    try:
        category = "nature"
        data = image_generator(category)
        caption = f"ℹ️ {data['descr']}\n\n"
        caption += f"❤️ {data['likes']}"
        await call.message.delete()
        await call.message.answer_photo(photo=data['image'], caption=caption, reply_markup=back_btn)
        await call.answer(cache_time=60)
    except:
        await call.message.answer("Bu kategoriya bo'yicha rasm topilmadi ! Yana tanlab ko'ring topishga harakat qilaman yoki \n\nPastdan bo'limni tanlang !", reply_markup=inline_markup)
        await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_markup)
    await call.answer()