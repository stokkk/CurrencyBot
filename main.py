import asyncio
import aiohttp
import aiogram

import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5972665711:AAF9-w-LbRSJVtNwhK1wLqqn45jehbd52IA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def gen_answer(message: str):
    if message == "Hello!":
        return "Hi"
    else:
        return "Sorry. I don't understand you."


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(gen_answer(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



