import pytest
import allure
import requests
from data import *
from helpers import *


class TestCreateCourier:

    @allure.title('Позитивная проверка создания курьера')
    @allure.description('Проверяется статус код и тело ответа')
    def test_create_courier_true(self):
        payload = generate_random_payload()
        r = requests.post(MAIN_URL + 'courier', data=payload)
        assert r.status_code == 201 and r.text == '{"ok":true}'

    @allure.title('Проверка однократной возможности создания курьера')
    @allure.description('Проверяется возвращение ошибки при создании курьера с существующим логином')
    def test_create_courier_once(self):
        payload = generate_random_payload()
        requests.post(MAIN_URL + 'courier', data=payload)
        r = requests.post(MAIN_URL + 'courier', data=payload)
        assert r.status_code == 409 and r.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    body = [{
        "password": "test_password",
        "firstName": "test_name"
    }, {
        "login": "test_login_name",
        "firstName": "test_name"
    }]

    @allure.title('Проверка обязательных полей при создании курьера')
    @allure.description('Проверяется возвращение ошибки при отсутствии обязательного поля в запросе')
    @pytest.mark.parametrize('body', body)
    def test_create_courier_without_required_field(self, body):
        r = requests.post(MAIN_URL + 'courier', data=body)
        assert r.status_code == 400 and r.json()['message'] == 'Недостаточно данных для создания учетной записи'
