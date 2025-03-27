import pytest
from base.courier import Courier

@pytest.fixture
def new_courier():
    login = Courier.generate_random_string()
    password = Courier.generate_random_string()
    first_name = Courier.generate_random_string()
    response = Courier.create(login, password, first_name)
    assert response.status_code == 201, f"Ошибка создания курьера: {response.text}"
    courier_data = {"login": login, "password": password, "first_name": first_name}
    login_response = Courier.login(login, password)
    assert login_response.status_code == 200, f"Ошибка авторизации курьера: {login_response.text}"
    courier_id = login_response.json().get("id")
    courier_data["id"] = courier_id
    yield courier_data
    Courier.delete(courier_id)
