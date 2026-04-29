from fastapi.testclient import TestClient
from my_app.main import app  # Предполагается, что объект app объявлен в my_app/main.py
import pytest

@pytest.fixture
def client():
    return TestClient(app)