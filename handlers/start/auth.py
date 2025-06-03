from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from core.dictionary import *

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):

    return message.answer(text=choice_lang)


