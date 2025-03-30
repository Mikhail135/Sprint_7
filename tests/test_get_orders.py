from base.order import Order
import allure

class GetOrder:
    @allure.feature("Заказы")
    @allure.title("Получение списка заказов")
    def test_get_orders():
        response = Order.get_orders()
        assert response.status_code == 200
        assert "orders" in response.json()