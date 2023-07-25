from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"title": "Hello World"}

def test_read_products():
    response = client.get("/products", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        {"id": 1, "name": "iPad", "price": 599},
        {"id": 2, "name": "iPhone", "price": 999},
        {"id": 3, "name": "iWatch", "price": 699}
    }