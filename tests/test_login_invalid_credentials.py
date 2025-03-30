from base.courier import Courier
import allure

class LoginInvalid:
    @allure.feature("Курьеры")
    @allure.title("Ошибка авторизации с неверными данными")
    def test_login_invalid_credentials():
        response = Courier.login("wrong_login", "wrong_pass")
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text