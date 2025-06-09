from core.database import async_session
from core.models import UsersModel
from sqlalchemy import select


async def get_users_list():
    async with async_session() as session:
        result = await session.execute(select(UsersModel))
        users = result.scalars().all()
        return users or None


async def get_user(chat_id: int):
    async with async_session() as session:
        user = await session.scalar(select(UsersModel).where(UsersModel.chat_id == chat_id))
        return user or None


async def create_user(query):
    async with async_session() as session:
        session.add(query)
        await session.commit()


async def is_user_authenticated(chat_id: int) -> bool:
    async with async_session() as session:
        user = await session.scalar(
            select(UsersModel).where(UsersModel.chat_id == chat_id)
        )
        return bool(user)


async def update_user(chat_id: int, query):
    async with async_session() as session:
        user = await session.scalar(select(UsersModel).where(UsersModel.chat_id == chat_id))
        if user:
            user.full_name = query.full_name
            user.phone_number = query.phone_number
            user.chat_id = query.chat_id
            user.counterparty_id = query.counterparty_id
            await session.commit()
            return True
        return False

