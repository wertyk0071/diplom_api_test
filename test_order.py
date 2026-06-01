# Владимир Пахомов, 43-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import pytest

BASE_URL = "https://47f687a3-d97f-45f5-be7b-81b30a69b5e0.serverhub.praktikum-services.ru"

def test_create_and_get_order():
    # создаём заказ
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    create_resp = requests.post(BASE_URL + "/api/v1/orders", json=order_data)
    track = create_resp.json()["track"]

    # получаем заказ по треку
    get_resp = requests.get(BASE_URL + "/api/v1/orders/track?t=" + str(track))
    
    # проверяем, что код 200
    assert get_resp.status_code == 200