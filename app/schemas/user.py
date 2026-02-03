from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_passwrd(cls, v: str) -> str:
        byte_len = len(v.encode("utf-8"))

        if byte_len > 72:
            raise ValueError("Password must not exceed 72 bytes")

        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        
        return v

class UserPublic(BaseModel):
    id: str
    email: EmailStr
    full_name: str | None = None
    is_active: bool
    is_verified: bool

    class Config:
        from_attributes = True