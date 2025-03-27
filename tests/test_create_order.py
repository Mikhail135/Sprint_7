import pytest

from base.order import Order
import allure

@allure.feature("Заказы")
@allure.story("Создание заказа с разными вариантами цветов")
@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def test_create_order(color):
    payload = {
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St",
        "metroStation": 4,
        "phone": "+7 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-01",
        "comment": "Test order",
        "color": color
    }
    response = Order.create(payload)
    assert response.status_code == 201
    assert "track" in response.json()
