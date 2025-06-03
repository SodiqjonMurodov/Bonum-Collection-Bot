from dotenv import load_dotenv
import os
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


load_dotenv()

class Settings:
    def __init__(self):
        self.__BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.__MOYSKLAD_TOKEN = os.getenv("MOYSKLAD_TOKEN")
        self.__BASE_URL = os.getenv("BASE_URL")

        # Database variables
        self.__DB_NAME = os.getenv("DB_NAME")
        self.__DB_USER = os.getenv("DB_USER")
        self.__DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.__DB_HOST = os.getenv("DB_HOST")
        self.__DB_PORT = os.getenv("DB_PORT")


    def get_bot(self):
        return Bot(
            token=self.__BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML
            )
        )

    def get_db_url(self):
        return f"postgresql+asyncpg://{self.__DB_USER}:{self.__DB_PASSWORD}@{self.__DB_HOST}:{self.__DB_PORT}/{self.__DB_NAME}"

    def get_moysklad_token(self):
        return self.__MOYSKLAD_TOKEN

    def get_base_url(self):
        return self.__BASE_URL


settings = Settings()

