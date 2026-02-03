from httpx import AsyncClient
import pytest
from tests.unique_email import unique_email

@pytest.mark.asyncio
async def test_login_returns_token(client:AsyncClient):
    email = unique_email()

    await client.post(
        "/auth/signup",
        json={
            "email": email,
            "password": "password123",
        },
    )

    res = await client.post(
        "/auth/login",
        json={
            "email": email,
            "password": "password123",
        },
    )

    assert res.status_code == 200
    body = res.json()

    assert "access_token" in body
    assert body["token_type"] == "bearer"
