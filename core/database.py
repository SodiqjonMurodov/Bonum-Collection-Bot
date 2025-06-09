from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import settings
from core.models import Base


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    # echo=True,
    future=True,
    # pool_size=5,
    # max_overflow=10,
)
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def async_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)