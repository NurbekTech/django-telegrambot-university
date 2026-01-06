import asyncio
import requests
import logging


from decouple import config

from aiogram import Bot, Dispatcher
from apps.handlers import router


BOT_TOKEN = config("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit BOT")
