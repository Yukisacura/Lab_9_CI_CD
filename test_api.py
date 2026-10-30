import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    
    assert response.status_code == 200, "Ожидался статус 200"
    
    data = response.json()
    assert "data" in data, "Отсутствует ключ data в ответе"
    assert data["data"]["id"] == 2, "Неверный ID пользователя"
    assert data["data"]["first_name"] == "Janet", "Неверное имя пользователя"

def test_create_user():
    payload = {"name": "mira", "job": "qa"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    assert response.status_code == 201, "Ожидался статус 201"
    
    data = response.json()
    assert data["name"] == "mira", "Имя не совпадает"
    assert data["job"] == "qa", "Профессия не совпадает"
    assert "id" in data, "Сервер не вернул ID созданного юзера"

def test_update_user():
    payload = {"name": "mira", "job": "senior qa"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    
    assert response.status_code == 200, "Ожидался статус 200"
    
    data = response.json()
    assert data["job"] == "senior qa", "Данные не обновились"