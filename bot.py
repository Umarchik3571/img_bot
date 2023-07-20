import logging

from aiogram import Bot,Dispatcher,executor, types
from aiogram.types import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import img_btn

logging.basicConfig(level=logging.INFO)

BOT_TOKEN="6065128506:AAHmEopp3K5bmHbmb2sumu5vrz6CYHnmi2k"

bot=Bot(token=BOT_TOKEN)
storage=MemoryStorage()
dp=Dispatcher(bot=bot,storage=storage)

images=["d.jpg","f.jpg","h.jpg"]

@dp.message_handler(commands=['start'])
async def start_bot(message:Message):
    await message.answer("Salom.\n\nGallery: /img")

@dp.message_handler(commands=['img'])
async def img_gallery(message:Message,state:FSMContext):
    btn = await img_btn(1,len(images))
    await state.update_data(page=1)
    await message.answer_photo(InputFile("d.jpg"),reply_markup=btn)
    

if __name__=="__main__":
    executor.start_polling(dp)


