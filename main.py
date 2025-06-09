import asyncio
import logging
import sys
from aiogram import Dispatcher
from core.config import settings
from core.database import async_db
from handlers.start import auth, middleware


async def main():
    # Creating async db
    await async_db()

    # Connection to db
    dp = Dispatcher()

    # I18n localization
    dp.message.middleware(middleware.I18nMiddleware())
    dp.callback_query.middleware(middleware.I18nMiddleware())

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

