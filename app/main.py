from fastapi import FastAPI
from sqlalchemy import text
from contextlib import asynccontextmanager
from app.db import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    yield
    # Shutdown code

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}