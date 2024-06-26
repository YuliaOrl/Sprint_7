import allure
from data import *
from helpers import *


class TestOrderList:

    @classmethod
    def setup_class(cls):
        courier = register_new_courier_and_return_login_password()
        payload = {
            "login": courier[0],
            "password": courier[1]
        }
        login_response = requests.post(MAIN_URL + 'courier/login', data=payload)
        cls.courier_id = login_response.json()["id"]

    @allure.title('Позитивная проверка получения списка заказов курьера по его ID')
    @allure.description('Проверяется статус код и возвращение в теле ответа списка заказов')
    @allure.step('Получение списка заказов курьера')
    def test_order_list_with_courier_id(self):
        response = requests.get(MAIN_URL + 'orders?courierId=' + str(self.courier_id))
        assert response.status_code == 200 and response.json()['orders'] == []

    @classmethod
    def teardown_class(cls):
        requests.delete(MAIN_URL + 'courier/' + str(cls.courier_id), data={"id": f'{cls.courier_id}'})
