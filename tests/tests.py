from starlette.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_root_endpoint():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}

