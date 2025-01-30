from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.settings import Settings

engine = create_async_engine(url=Settings().db_url, future=True, echo=True, pool_pre_ping=True)

AsyncSessionMaker = async_sessionmaker(
    bind=engine,
    autocommit=False,
    expire_on_commit=False
)


async def async_connect() -> AsyncSession:
    async with AsyncSessionMaker as session:
        yield session
