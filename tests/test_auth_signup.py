from httpx import AsyncClient
import pytest

from tests.unique_email import unique_email

@pytest.mark.asyncio
async def test_signup_success(client:AsyncClient):
    email = unique_email()
    
    res = await client.post(
        "/auth/signup",
        json={
            "email": email,
            "password": "correcthorsebatterystaple",
        },
    )

    assert res.status_code == 201
    body = res.json()
    assert body["email"] == email
    assert body["is_active"] is True
