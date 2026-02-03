from httpx import AsyncClient
import pytest

from tests.unique_email import unique_email

@pytest.mark.asyncio
async def test_me_requires_auth(client:AsyncClient):
    res = await client.get("/users/me")
    assert res.status_code == 401


@pytest.mark.asyncio
async def test_me_with_token(client:AsyncClient):
    email = unique_email()
    
    await client.post(
        "/auth/signup",
        json={
            "email": email,
            "password": "password123",
        },
    )

    login = await client.post(
        "/auth/login",
        json={
            "email": email,
            "password": "password123",
        },
    )

    token = login.json()["access_token"]

    res = await client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert res.status_code == 200
    body = res.json()
    assert body["email"] == email
