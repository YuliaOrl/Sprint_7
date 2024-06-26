import pytest
import allure
import requests
import json
from data import *


class TestCreateOrder:
    color = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]

    @allure.title('Проверка создания заказа')
    @allure.description('Проверяется создание заказа с указанием разных вариантов цвета самоката')
    @allure.step('Создание заказа с выбором цвета самоката {color}')
    @pytest.mark.parametrize('color', color)
    def test_create_order_true(self, color):
        payload = {
            "firstName": "Ольга",
            "lastName": "Петрова",
            "address": "Москва",
            "metroStation": 5,
            "phone": "+78003553535",
            "rentTime": 5,
            "deliveryDate": "2027-07-30",
            "comment": "Быстрая доставка",
            "color": color
        }
        r = requests.post(MAIN_URL + 'orders', data=json.dumps(payload))
        assert r.status_code == 201 and r.json()['track']
