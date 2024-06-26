import requests
import random
import string


def generate_random_str(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_payload():
    login = generate_random_str(10)
    password = generate_random_str(10)
    first_name = generate_random_str(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


def register_new_courier_and_return_login_password():
    login_pass = []
    payload = generate_random_payload()
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    if response.status_code == 201:
        login_pass.append(payload["login"])
        login_pass.append(payload["password"])
        login_pass.append(payload["firstName"])
    return login_pass
