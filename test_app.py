import pytest
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as flask_app

@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c

def test_get_todos_empty(client):
    res = client.get("/api/todos")
    assert res.status_code == 200
    assert res.get_json() == []

def test_add_todo(client):
    res = client.post("/api/todos",
        data=json.dumps({"text": "Buy milk"}),
        content_type="application/json")
    assert res.status_code == 201
    data = res.get_json()
    assert data["text"] == "Buy milk"
    assert data["done"] is False
    assert data["id"] == 1

def test_toggle_todo(client):
    client.post("/api/todos",
        data=json.dumps({"text": "Exercise"}),
        content_type="application/json")
    res = client.patch("/api/todos/1")
    assert res.status_code == 200
    assert res.get_json()["done"] is True

def test_delete_todo(client):
    client.post("/api/todos",
        data=json.dumps({"text": "Delete me"}),
        content_type="application/json")
    res = client.delete("/api/todos/1")
    assert res.status_code == 200
    todos = client.get("/api/todos").get_json()
    assert todos == []

def test_toggle_not_found(client):
    res = client.patch("/api/todos/999")
    assert res.status_code == 404

def test_index_page(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Tasks" in res.data