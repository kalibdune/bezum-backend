import pytest
import pytest_asyncio

from bezum.config import config
from bezum.db.session import SessionManager


@pytest_asyncio.fixture(scope="function")
async def get_session(prepare_tables):
    session_manager = SessionManager(config.postgres.get_dsn, config.postgres.debug)
    async with session_manager.session() as session:
        yield session
    session_manager._engine
