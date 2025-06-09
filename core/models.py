from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import BigInteger, String, DateTime, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class UsersModel(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chat_id: Mapped[int] = mapped_column(BigInteger)
    api_id: Mapped[int]  = mapped_column(BigInteger)
    full_name: Mapped[str] = mapped_column(String(250))
    phone_number: Mapped[str] = mapped_column(String(13))
    is_admin: Mapped[bool] = mapped_column(default=False)
    lang: Mapped[str] = mapped_column(String(2))
    region: Mapped[str] = mapped_column(String(20))


