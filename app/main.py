from fastapi import FastAPI

from app.internal.lifespan import lifespan
from app.routers import students


app = FastAPI(lifespan=lifespan)
app.include_router(students.router)


@app.get("/")
async def ping():
    return {"message": "pong"}
