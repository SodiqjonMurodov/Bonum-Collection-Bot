from core.database import async_session
from core.models import RegionsModel
from sqlalchemy import select


async def get_regions_list():
    async with async_session() as session:
        result = await session.execute(select(RegionsModel))
        users = result.scalars().all()
        return users or None