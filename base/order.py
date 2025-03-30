import requests
from data import data
import allure

class Order:
    @staticmethod
    @allure.step("Создание заказа")
    def create(payload):
        return requests.post(f"{data.BASE_URL}/orders", json=payload)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders():
        return requests.get(f"{data.BASE_URL}/orders")

