from fastapi import FastAPI

from app.internal.lifespan import lifespan
from app.routers import security, students


app = FastAPI(lifespan=lifespan)
app.include_router(students.router)
app.include_router(security.router)


@app.get("/")
async def ping():
    return {"message": "pong"}
