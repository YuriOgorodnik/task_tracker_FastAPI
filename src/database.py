from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

# URL для подключения к базе данных
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

metadata = MetaData()

engine = create_async_engine(DATABASE_URL)  # Создание асинхронного движка базы данных
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)  # Создание фабрики сессий для асинхронной работы


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    # Автоматическое управление сессией с использованием async_session_maker
    async with async_session_maker() as session:
        yield session  # Возврат асинхронной сессии в виде генератора для использования в асинхронном контексте
