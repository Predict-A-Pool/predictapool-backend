from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.base import Base

import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        String(36),
        primary_key=True, 
        default=uuid.uuid4
    )

    email: Mapped[str] = mapped_column(
        String(100), 
        unique=True, 
        nullable=False,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(100), 
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )