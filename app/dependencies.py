from fastapi import Request


async def get_db(request: Request):
    async_session = request.app.state.async_session
    async with async_session() as session:
        yield session
        await session.rollback()
