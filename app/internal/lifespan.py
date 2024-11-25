from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.startup import setup_db, shutdown_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_db(app)
    yield
    await shutdown_db(app)
