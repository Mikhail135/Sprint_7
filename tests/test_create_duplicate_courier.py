from base.courier import Courier
import allure

@allure.feature("Курьеры")
@allure.story("Попытка создать дублирующего курьера")
def test_create_duplicate_courier(new_courier):
    response = Courier.create(new_courier["login"], new_courier["password"], Courier.generate_random_string())
    assert response.status_code == 409
    assert "Этот логин уже используется" in response.text
