import json
from starlette import status


test_data = {
    "name": "test_name",
    "latitude": 0,
    "longitude": 0,
    "address": "string",
    "city": "string"
}


def test_create_shop(client):
    response = client.post("/shops/", json=test_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get('name') == test_data.get('name')


def test_get_shops(client):
    response = client.get("/shops/")
    assert response.status_code == status.HTTP_200_OK
    assert bool(response.json())


def test_get_shop(client):
    data = {
        "name": "test_get_shop_name",
        "latitude": 0,
        "longitude": 0,
        "address": "string",
        "city": "string"
    }
    shop = client.post("/shops/", json=data)
    response = client.get(f'/shop/{shop.json().get("id")}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get('name') == shop.json().get('name')


def test_delete_shop(client):
    data = {
        "name": "test_delete_shop_name",
        "latitude": 0,
        "longitude": 0,
        "address": "string",
        "city": "string"
    }
    shop = client.post("/shops/", json=data)
    response = client.delete(f'/shop/{shop.json().get("id")}/')
    assert response.status_code == status.HTTP_202_ACCEPTED
