from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_query import category_callback

categories = {
    "🎨 San'at": "art",
    "🚘 Avtomobil": "vehicle",
    "✈️ Sayohat": 'travel',
    "🌂 Ekskluziv": "work",
    "🌍 So'nggi yangiliklar": "current_events",
    "🏕 Tabiat": "nature"
}

inline_markup = InlineKeyboardMarkup(row_width=2)

back_btn = InlineKeyboardMarkup(row_width=1)
back = InlineKeyboardButton(text="🔙 Ortga", callback_data='cancel')
back_btn.insert(back)

for key,value in categories.items():
    inline_markup.insert(InlineKeyboardButton(text=key, callback_data=category_callback.new(item_name=value)))