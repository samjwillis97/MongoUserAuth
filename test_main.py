import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_register_new_user():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        response = await ac.post(
            "/api/auth/register",
            json={
                "email": "user@example.com",
                "password": "string"
            }
        )
    assert response.status_code == 201
    # id
    # email
    # is_active
    # is_superuser
    # permissions
    # assert response.content['email'] == "user@example.com"
    # assert response.json() == {"msg": "Hello World"}
