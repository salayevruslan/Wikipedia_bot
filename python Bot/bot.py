import asyncio
import logging
from aiogram import Bot, Dispatcher, types , F 
from aiogram.filters.command import Command
import wikipedia 
from add_bot import add_bot

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7106268558:AAFh4oBFlkbw2uKc46g6LXtrm3ulH1jWKJc")

dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    tg_id = message.from_user.id
    username = message.from_user.username
    fullname = message.from_user.full_name
    add_bot(ID =tg_id , FULL_NAME = fullname , USERNAME=username)
    await message.answer(f"Assalomu aleykum {fullname}")
    

@dp.message(F.text.lower() == "Salom")
async def Info(message: types.Message ) : 
    fullname = message.from_user.full_name
    await message.reply(f"Qidirmoqchi bo'lgan narsangizni yozing {fullname}")
    
@dp.message(F.text)
async def Wikipediabot(message :types.Message):
    text = message.text 
    wikipedia.set_lang('uz')
    try:
        malumot = wikipedia.summary(text)
        await message.reply(text=malumot)
    except:
        await message.answer("Ma'lumot topilmadi !")
    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Bot faol")