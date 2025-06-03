from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from core.config import settings
from core.models import Base


DATABASE_URL = settings.get_db_url()

# Creating an asynchronous engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True  # Setting: If True, outputs SQL logs (optional)
)

# Session maker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # Objects remain valid after session commit
)

# Creating DB
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)