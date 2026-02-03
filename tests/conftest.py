import asyncio
import os
import pytest
from dotenv import load_dotenv

load_dotenv(".env.test", override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

assert DATABASE_URL is not None
assert "test" in DATABASE_URL.lower(), (
    "Tests are not using a test database!"
)

from httpx import AsyncClient

from app.db.session import engine
from app.db.base import Base

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest.fixture
async def client():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        yield ac
