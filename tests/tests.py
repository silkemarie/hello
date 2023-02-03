from starlette.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_read_root():
    # when
    res = client.get("/")

    # then
    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}


def test_create_student_positive_id():
    # given
    json_blob = {"student_id": 1, "name": "Jens"}

    # when
    res = client.post("/students/", json=json_blob)

    # then
    assert res.status_code == 200


def test_create_student_negative_id():
    # given
    json_blob = {"student_id": -1, "name": "Jens"}

    # when
    res = client.post("/students/", json=json_blob)

    # then
    assert res.status_code != 200
