import asyncio
import logging
import sys
from aiogram import Dispatcher
from core.config import settings
from core.database import init_db
from handlers.start import auth


async def main():
    # Creating async db
    await init_db()

    # Connection to db
    dp = Dispatcher()

    # Routers
    dp.include_routers(
        auth.router,

    )
    await dp.start_polling(settings.get_bot())


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler(sys.stdout)
        ]
)  # logging
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

