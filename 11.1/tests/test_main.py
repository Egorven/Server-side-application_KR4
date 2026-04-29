def test_create_user(client):
    response = client.post("/users", json={"age": 16, "username": "Jhon"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "username": "Jhon", "age": 16}

def test_create_user_param_error(client):
    response = client.post("/users", json={"age": 16})
    assert response.status_code == 422

def test_create_user_validation_error(client):
    response = client.post("/users", json={"age": "one", "username": "Jhon"})
    assert response.status_code == 422

def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "Jhon", "age": 16}

def test_get_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404
def test_get_user_invalid_request(client):
    response = client.get("/users/a")
    assert response.status_code == 422

def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == 204

def test_delete_user_not_found(client):
    response = client.delete("/users/15")
    assert response.status_code == 404

def test_delete_user_invalid_reqest(client):
        response = client.delete("/users/a")
        assert response.status_code == 422

def test_delete_user_invalid_request(client):
    response = client.delete("/users/a")
    assert response.status_code == 422
    body = response.json()
    assert "detail" in body
    assert body["detail"][0]["loc"] == ["path", "user_id"]