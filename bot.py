import datetime
import time

import requests
from aiogram import Bot, types
from aiogram import Dispatcher

import logging

from aiogram.utils import executor

TOKEN = "token here"
bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


@dp.my_chat_member_handler(chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def start(my_chat_member: types.ChatMemberUpdated):
    chat_id = my_chat_member.chat.id

    await bot.send_message(chat_id=chat_id, text='Я повідомлю, коли MISA знову запрацює😉')

    website_down = True
    while website_down:
        try:
            requests.get('http://misa.meduniv.lviv.ua/')
            website_down = False
            await bot.send_message(chat_id=chat_id, text='MISA запрацювала!')
            print('запрацювала!')
        except:
            print(f'досі лежить. {datetime.datetime.now()}')
            time.sleep(60)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
