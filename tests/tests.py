from starlette.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_root_endpoint():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}

def test_positive_id():
    json_blob = {"student_id": 1, "name": "Jens"}
    res = client.post("/students/", json=json_blob)
    assert res.status_code == 200

def test_negative_id():
    json_blob = {"student_id": -1, "name": "Jens"}
    res = client.post("/students/", json=json_blob)
    assert res.status_code != 200