from base.courier import Courier
import allure
import pytest


class TestCreateCourier:
    @allure.feature("Курьеры")
    @allure.title("Создание курьера с валидными данными")
    def test_create_courier_successfully(self):
        login = Courier.generate_random_string()
        password = Courier.generate_random_string()
        first_name = Courier.generate_random_string()
        response = Courier.create(login, password, first_name)
        assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}"
        assert response.json().get("ok") is True, f"Ответ API: {response.json()}"

    @pytest.mark.parametrize("missing_field", ["login", "password", "first_name"])
    @allure.feature("Курьеры")
    @allure.title("Создание курьера без обязательного поля")
    def test_create_courier_missing_field(self, missing_field):
        data = {
            "login": Courier.generate_random_string(),
            "password": Courier.generate_random_string(),
            "first_name": Courier.generate_random_string(),
        }
        del data[missing_field]
        response = Courier.create(**data)
        if missing_field == "first_name":
            assert response.status_code == 201
        else:
            assert response.status_code == 400
            assert "message" in response.json()
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
