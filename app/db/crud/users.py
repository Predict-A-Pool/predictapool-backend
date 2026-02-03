from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.models.user import User
from app.security.passwords import hash_password

def create_user(db: Session, email: str, password: str) -> User:
    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("User with this email already exists")
    
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    result = db.execute(stmt)
    return result.scalar_one_or_none()