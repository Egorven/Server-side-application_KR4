import pytest
from httpx import ASGITransport, AsyncClient
import asyncio
from faker import Faker

from main import app, db

fake = Faker()

@pytest.fixture(autouse=True)
def clear_db():
    from main import db
    db.clear()
    yield
    db.clear()

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/users", json={"age": fake.random_int(18, 90), "username": fake.user_name()})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "username": response.json()["username"], "age":response.json()["age"]}

@pytest.mark.asyncio
async def test_get_user():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        post = await ac.post("/users", json={"age": fake.random_int(18, 90), "username": fake.user_name()})
        assert post.status_code == 201
        user_id = post.json()["id"]
        response = await ac.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": user_id, "username": post.json()["username"], "age": post.json()["age"]}

@pytest.mark.asyncio
async def test_get_user_not_found():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/users/999")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
           post = await ac.post("/users", json={"age": fake.random_int(18, 90), "username": fake.user_name()})
           assert post.status_code == 201
           user_id = post.json()["id"]
           response = await ac.delete(f"/users/{user_id}")
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_delete_user_not_found():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.delete("/users/1")
    assert response.status_code == 404
