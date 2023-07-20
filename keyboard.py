from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def img_btn(current_img,total_img):
    btn = InlineKeyboardMarkup()
    btn.add(
        
        InlineKeyboardButton("👈",callback_date="0"),
        InlineKeyboardButton(f"{current_img}/{total_img}",callback_data="prev"),
        InlineKeyboardButton("👉",callback_date="next"),
    )
    return btn