import os
from datetime import timedelta

_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if not _SECRET_KEY:
    raise RuntimeError("JWT_SECRET_KEY is not set")

JWT_SECRET_KEY = _SECRET_KEY

JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

ACCESS_TOKEN_EXPIRE_DELTA = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)