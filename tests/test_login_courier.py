import pytest
import allure
from data import *
from helpers import *


class TestLoginCourier:
    courier = register_new_courier_and_return_login_password()
    payload = {
        "login": courier[0],
        "password": courier[1]
    }

    @allure.title('Позитивная проверка авторизации курьера')
    @allure.description('Проверяется статус код и возвращение id в теле ответа')
    @allure.step('Авторизация курьера с корректными данными')
    def test_login_courier_true(self):
        r = requests.post(MAIN_URL + 'courier/login', data=self.payload)
        assert r.status_code == 200 and r.json()['id']

    payload_data = [[{"login": courier[0]}, 504, "Service unavailable"],
                    [{"password": courier[1]}, 400, "Недостаточно данных для входа"]]

    @allure.title('Проверка обязательных полей при авторизации курьера')
    @allure.description('Проверяется возвращение ошибки при отсутствии обязательного поля в запросе')
    @allure.step('Авторизация курьера с параметрами {body}')
    @pytest.mark.parametrize('body, code, message', payload_data)
    def test_login_courier_without_required_field(self, body, code, message):
        r = requests.post(MAIN_URL + 'courier/login', data=body)
        assert r.status_code == code and message in r.text

    body = [{
        "login": courier[0][0:-1],
        "password": courier[1]
    }, {
        "login": courier[0],
        "password": courier[1][0:-1]
    }]

    @allure.title('Негативная проверка авторизации курьера')
    @allure.description('Проверяется возвращение ошибки при неверном логине или пароле')
    @allure.step('Авторизация курьера с неверными параметрами {body}')
    @pytest.mark.parametrize('body', body)
    def test_login_courier_with_incorrect_login_or_password(self, body):
        r = requests.post(MAIN_URL + 'courier/login', data=body)
        assert r.status_code == 404 and r.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Негативная проверка авторизации курьера под несуществующим пользователем')
    @allure.description('Проверяется возвращение ошибки при несуществующем логине и пароле')
    @allure.step('Авторизация курьера с несуществующей парой логин-пароль')
    def test_login_courier_non_existent_user(self):
        payload = {
            "login": "non_existent_user",
            "password": "non_existent_password"
        }
        r = requests.post(MAIN_URL + 'courier/login', data=payload)
        assert r.status_code == 404 and r.json()['message'] == 'Учетная запись не найдена'

    @classmethod
    def teardown_class(cls):
        login_response = requests.post(MAIN_URL + 'courier/login', data=cls.payload)
        courier_id = login_response.json()["id"]
        requests.delete(MAIN_URL + 'courier/' + str(courier_id), data={"id": f'{courier_id}'})
