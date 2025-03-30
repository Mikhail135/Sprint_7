import pytest
from base.courier import Courier


@pytest.fixture
def new_courier():
    login = Courier.generate_random_string()
    password = Courier.generate_random_string()
    first_name = Courier.generate_random_string()

    response = Courier.create(login, password, first_name)
    if response.status_code != 201:
        raise Exception(f"Ошибка создания курьера: {response.text}")

    courier_data = {"login": login, "password": password, "first_name": first_name}

    login_response = Courier.login(login, password)
    if login_response.status_code != 200:
        raise Exception(f"Ошибка авторизации курьера: {login_response.text}")

    courier_id = login_response.json().get("id")
    if not courier_id:
        raise Exception("Не удалось получить ID курьера после авторизации")

    courier_data["id"] = courier_id
    yield courier_data

    Courier.delete(courier_id)
