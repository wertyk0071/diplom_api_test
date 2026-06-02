# для запросов

import requests
from .config import BASE_URL, ORDERS_ENDPOINT, GET_ORDER_BY_TRACK

def create_order(order_data):
    url = BASE_URL + ORDERS_ENDPOINT
    response = requests.post(url, json=order_data)
    return response

def get_order_by_track(track_number):
    url = BASE_URL + GET_ORDER_BY_TRACK
    params = {"t": track_number}
    response = requests.get(url, params=params)
    return response