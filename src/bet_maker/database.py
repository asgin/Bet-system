from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from src.bet_maker.config import settings

engine = create_async_engine(settings.DB_URL, echo=True)
session = async_sessionmaker(engine, autocommit=False, autoflush=False, expire_on_commit=False)
Base = declarative_base()

async def get_db() -> AsyncSession:
    async with session() as db:
        yield db