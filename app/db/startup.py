import logging

from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from app.internal.config import settings

log = logging.getLogger(__name__)


async def setup_db(app: FastAPI) -> None:
    database_uri = settings.database_uri
    if not database_uri:
        raise ValueError("Database uri not set; aborting startup")
    engine = create_async_engine(database_uri.unicode_string(), echo=True)
    async with engine.connect() as conn:
        try:
            await conn.execute(text("SELECT 1"))
        except Exception:
            log.exception("An error occurred while testing db connection")

    app.state.db_engine = engine
    app.state.async_session = async_sessionmaker(engine, expire_on_commit=False)


async def shutdown_db(app: FastAPI) -> None:
    await app.state.db_engine.dispose()
