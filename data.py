MAIN_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
COURIER_URL = MAIN_URL + '/courier'
LOGIN_URL = COURIER_URL + '/login'
ORDERS_URL = MAIN_URL + '/orders'
ORDER_ID_URL = ORDERS_URL + '?courierId='

CREATE_EXPECTED_MESSAGE_201 = '{"ok":true}'
CREATE_EXPECTED_MESSAGE_400 = 'Недостаточно данных для создания учетной записи'
CREATE_EXPECTED_MESSAGE_409 = 'Этот логин уже используется. Попробуйте другой.'
LOGIN_EXPECTED_MESSAGE_400 = 'Недостаточно данных для входа'
LOGIN_EXPECTED_MESSAGE_404 = 'Учетная запись не найдена'
LOGIN_EXPECTED_MESSAGE_504 = 'Service unavailable'

ORDER_DATA = {
    "firstName": "Ольга",
    "lastName": "Петрова",
    "address": "Москва",
    "metroStation": 5,
    "phone": "+78003553535",
    "rentTime": 5,
    "deliveryDate": "2027-07-30",
    "comment": "Быстрая доставка",
}

SCOOTER_COLOR = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]
