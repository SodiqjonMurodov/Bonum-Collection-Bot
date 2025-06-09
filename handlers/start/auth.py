from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.start.kb import get_phone_request_btn, get_region_request_btn
from handlers.start.state import RegStatesGroup
from core.dictionary import *
from queries.users import is_user_authenticated
from api.counterparty import check_counterparty_by_phone

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext, **kwargs):
    chat_id = message.from_user.id
    kb = None
    if not await is_user_authenticated(chat_id):
        kb = await get_region_request_btn()
        await state.set_state(RegStatesGroup.lang)
        return await message.answer(text=choice_lang_message, reply_markup=kb)

    return message.answer(text=main_menu_message, reply_markup=kb)


@router.message(F.contact, RegStatesGroup.phone_number)
async def got_phone_number(message: Message, state: FSMContext, **kwargs):
    phone_number = message.contact.phone_number
    user_id = message.contact.user_id
    await check_counterparty_by_phone("+998 (15) 157-96-36")
    return message.answer(text=phone_number)