from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.internal.lifespan import lifespan
from app.routers import security, students


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(students.router)
app.include_router(security.router)


@app.get("/")
async def ping():
    return {"message": "pong"}
