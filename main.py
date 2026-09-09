import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()


bot = Bot(token="8612457724:AAEW-7TvZWacADNx4Sq1WysVNCaxld_gyEcx")
dp = Dispatcher()
# print(f"Bot started with token: {os.getenv('BOT_TOKEN')}")


@dp.message()
async def echo(message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


print('salom')

print('authdan yozildi')
