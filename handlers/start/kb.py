from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from core.dictionary import *
from queries.regions import get_regions_list


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
        one_time_keyboard=True
    )


async def get_region_request_btn() -> ReplyKeyboardMarkup:
    # Bazadan barcha regionlarni olamiz
    regions = await get_regions_list()
    region_names = [region.name for region in regions]

    # Tugmalarni 2 ustunli qilib joylashtirish
    buttons = []
    row = []
    for i, name in enumerate(region_names, start=1):
        row.append(KeyboardButton(text=name))
        if i % 2 == 0:
            buttons.append(row)
            row = []
    if row:  # Agar oxirgi qatorda bitta tugma qolsa
        buttons.append(row)

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
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
