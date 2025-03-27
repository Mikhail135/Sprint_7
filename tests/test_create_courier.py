from base.courier import Courier
import allure

@allure.feature("Курьеры")
@allure.story("Создание курьера")
def test_create_courier():
    login = Courier.generate_random_string()
    password = Courier.generate_random_string()
    first_name = Courier.generate_random_string()
    response = Courier.create(login, password, first_name)
    assert response.status_code == 201
    assert response.json()["ok"] is True