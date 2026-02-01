from sqlalchemy import Engine, create_engine
from typing import Optional
import os

_engine: Optional[Engine] = None

def get_engine() -> Engine:
    global _engine
    
    if _engine is None:
        DATABASE_URL = os.getenv("DATABASE_URL")
        if DATABASE_URL is None:
            raise ValueError("DATABASE_URL environment variable is not set")
        _engine = create_engine(DATABASE_URL)
    return _engine