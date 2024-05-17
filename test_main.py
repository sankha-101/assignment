import pytest
from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_request():
    payload = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "batchid" in data
    assert "response" in data
    assert "status" in data
    assert "started_at" in data
    assert "completed_at" in data

def test_empty_list():
    payload = {
        "batchid": "id0102",
        "payload": [[]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [0]

def test_single_list():
    payload = {
        "batchid": "id0103",
        "payload": [[5]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [5]

def test_negative_numbers():
    payload = {
        "batchid": "id0104",
        "payload": [[-1, -2], [-3, -4]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [-3, -7]

def test_float_numbers():
    payload = {
        "batchid": "id0105",
        "payload": [[1.5, 2.5], [3.5, 4.5]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == [4, 8]

def test_invalid_request():
    payload = {
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 422

def test_empty_payload():
    payload = {
        "batchid": "id0106",
        "payload": []
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == []
