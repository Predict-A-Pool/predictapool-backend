from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user import User
from app.core.passwords import hash_password

async def create_user(db: AsyncSession, email: str, password: str) -> User:
    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)

    await db.commit()
    await db.refresh(user)
    
    return user

async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()