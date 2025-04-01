import pytest

from bezum.config import config
from bezum.db.models.base import Base
from bezum.db.session import SessionManager

# pytest raises
# mocker.Mock
# mock.patch
# pytest-vcr для кэширования ответа от реального внешнего сервиса при повторном прогоне тестов


session_manager = SessionManager(
    config.postgres.get_dsn_psycopg, config.postgres.debug, is_async=False
)
engine = session_manager._engine


@pytest.fixture
def prepare_tables():
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)
        conn.commit()
    yield
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
