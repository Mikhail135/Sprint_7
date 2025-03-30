import requests
import random
import string
from data import data
import allure

class Courier:
    @staticmethod
    def generate_random_string(length=10):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    @staticmethod
    @allure.step("Создание курьера")
    def create(login=None, password=None, first_name=None):
        payload = {}
        if login is not None:
            payload["login"] = login
        if password is not None:
            payload["password"] = password
        if first_name is not None:
            payload["firstName"] = first_name

        return requests.post(f"{data.BASE_URL}/courier", json=payload)

    @staticmethod
    @allure.step("Авторизация курьера")
    def login(login, password):
        payload = {"login": login, "password": password}
        return requests.post(f"{data.BASE_URL}/courier/login", json=payload)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete(courier_id):
        return requests.delete(f"{data.BASE_URL}/courier/{courier_id}")