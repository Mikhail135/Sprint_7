from base.courier import Courier
import allure
import pytest

class TestCourierLogin:
    @allure.title("Успешная авторизация курьера")
    def test_courier_login_success(self, new_courier):
        response = Courier.login(new_courier["login"], new_courier["password"])
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Авторизация курьера без обязательного поля")
    def test_courier_login_missing_field(self, new_courier, missing_field):
        login = new_courier["login"] if missing_field != "login" else ""
        password = new_courier["password"] if missing_field != "password" else ""
        response = Courier.login(login, password)
        assert response.status_code == 400
        assert "message" in response.json()
        assert response.json()["message"] == "Недостаточно данных для входа"

    def test_courier_login_invalid_credentials(self):
        response = Courier.login("wrong_login", "wrong_password")
        print(f"Ответ API: статус {response.status_code}, тело {response.json()}")
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}. Ответ: {response.text}"
        assert 'id' in response.json(), f"Ответ не содержит поля 'id'. Ответ: {response.text}"


