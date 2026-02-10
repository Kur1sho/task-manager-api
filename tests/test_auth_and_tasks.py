def register_user(client, email: str, password: str):
    return client.post("/auth/register", json={"email": email, "password": password})

def login_user(client, email: str, password: str):
    # OAuth2PasswordRequestForm expects form-encoded: username + password
    return client.post(
        "/auth/login",
        data={"username": email, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}

def test_register_and_login_returns_token(client):
    r = register_user(client, "a@test.com", "Password123!")
    assert r.status_code == 201

    r = login_user(client, "a@test.com", "Password123!")
    assert r.status_code == 200
    body = r.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"

def test_tasks_requires_auth(client):
    r = client.get("/tasks")
    assert r.status_code == 401  # missing token

def test_user_scoping_tasks(client):
    # user A
    register_user(client, "a2@test.com", "Password123!")
    token_a = login_user(client, "a2@test.com", "Password123!").json()["access_token"]

    # user B
    register_user(client, "b2@test.com", "Password123!")
    token_b = login_user(client, "b2@test.com", "Password123!").json()["access_token"]

    # A creates task
    r = client.post(
        "/tasks",
        json={"title": "A task", "description": "only A sees this", "status": "todo"},
        headers=auth_headers(token_a),
    )
    assert r.status_code == 201
    task_a_id = r.json()["id"]

    # B creates task
    r = client.post(
        "/tasks",
        json={"title": "B task", "description": "only B sees this", "status": "todo"},
        headers=auth_headers(token_b),
    )
    assert r.status_code == 201
    task_b_id = r.json()["id"]

    # A lists tasks -> should only see A task
    r = client.get("/tasks", headers=auth_headers(token_a))
    assert r.status_code == 200
    ids_a = [t["id"] for t in r.json()]
    assert task_a_id in ids_a
    assert task_b_id not in ids_a

    # B tries to fetch A's task directly -> should be 404 (scoped)
    r = client.get(f"/tasks/{task_a_id}", headers=auth_headers(token_b))
    assert r.status_code == 404

    # A deletes own task OK
    r = client.delete(f"/tasks/{task_a_id}", headers=auth_headers(token_a))
    assert r.status_code == 200
