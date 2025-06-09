from datetime import datetime, time
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import BigInteger, String, DateTime, Integer, ForeignKey, JSON, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @classmethod
    def uuid_pk(cls):
        return mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    @classmethod
    def created_at_col(cls):
        return mapped_column(DateTime, default=datetime.utcnow)

    @classmethod
    def updated_at_col(cls):
        return mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class RegionsModel(Base):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name_uz: Mapped[str] = mapped_column(String(255))
    name_ru: Mapped[str] = mapped_column(String(255))

    users = relationship("UsersModel", back_populates="region")
    branches = relationship("BranchesModel", back_populates="region")

    def __repr__(self):
        return f"<Region(id={self.id}, name={self.name_uz})>"


class UsersModel(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = Base.uuid_pk()
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    api_id: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(250))
    phone_number: Mapped[str] = mapped_column(String(13))
    is_admin: Mapped[bool] = mapped_column(default=False)
    lang: Mapped[str] = mapped_column(String(2))
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id", ondelete="SET NULL"), nullable=True)
    is_new: Mapped[bool] = mapped_column(default=True)
    caller_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),
                                                 ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at: Mapped[datetime] = Base.created_at_col()
    updated_at: Mapped[datetime] = Base.updated_at_col()

    region = relationship("RegionsModel", back_populates="users")
    caller = relationship("UsersModel", remote_side=[id])

    def __repr__(self):
        return f"<User(id={self.id}, full_name={self.full_name}, chat_id={self.chat_id})>"


class LinksModel(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<Link(id={self.id}, name={self.name})>"


class BranchesModel(Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name_uz: Mapped[str] = mapped_column(String)
    name_ru: Mapped[str] = mapped_column(String)
    photo: Mapped[str] = mapped_column(String)
    address_uz: Mapped[str] = mapped_column(String)
    address_ru: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String(13))
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id", ondelete="SET NULL"), nullable=True)
    start_time: Mapped[time] = mapped_column(Time)
    end_time: Mapped[time] = mapped_column(Time)

    region = relationship("RegionsModel", back_populates="branches")

    def __repr__(self):
        return f"<Branch(id={self.id}, name={self.name_uz})>"


class NewsModel(Base):
    __tablename__ = 'news'

    id: Mapped[uuid.UUID] = Base.uuid_pk()
    content_type: Mapped[str] = mapped_column(String)
    file_id: Mapped[str] = mapped_column(String, nullable=True)
    caption_uz: Mapped[str] = mapped_column(String)
    caption_entities_uz: Mapped[list] = mapped_column(JSON, nullable=True)
    caption_ru: Mapped[str] = mapped_column(String)
    caption_entities_ru: Mapped[list] = mapped_column(JSON, nullable=True)

    def __repr__(self):
        return f"<News(id={self.id}, type={self.content_type})>"

