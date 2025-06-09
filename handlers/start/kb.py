from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from core.dictionary import (
    phone_request_kb_text,
    phone_request_placeholder_text,

)


async def get_lang_request_btn() -> ReplyKeyboardMarkup:
    button = [
        [
            KeyboardButton(text=uz_lang_kb_text),
            KeyboardButton(text=ru_lang_kb_text),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=button,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=phone_request_placeholder_text
    )


async def get_phone_request_btn() -> ReplyKeyboardMarkup:
    button = [
        [KeyboardButton(text=phone_request_kb_text, request_contact=True)]
    ]
    return ReplyKeyboardMarkup(
        keyboard=button,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=phone_request_placeholder_text
    )
