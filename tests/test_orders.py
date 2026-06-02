# Владимир Пахомов, 43-я когорта — Финальный проект. Инженер по тестированию плюс
# сценарии и проверки
import pytest
import json
from .api_client import create_order, get_order_by_track

# JSON с тестовыми данными
with open("tests/test_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("order_key", ["valid_order"])
def test_create_and_get_order(order_key):
    order_data = test_data[order_key]

    create_resp = create_order(order_data)
    assert create_resp.status_code == 201, "Order creation failed"

    track = create_resp.json().get("track")
    assert track is not None, "No track in response"

    get_resp = get_order_by_track(track)
    assert get_resp.status_code == 200, f"Failed to get order, status {get_resp.status_code}"