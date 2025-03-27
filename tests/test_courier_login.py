from base.courier import Courier
import allure

def test_courier_login(new_courier):
    response = Courier.login(new_courier["login"], new_courier["password"])
    assert response.status_code == 200
    assert "id" in response.json()