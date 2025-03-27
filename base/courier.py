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
    def create(login, password, first_name):
        payload = {"login": login, "password": password, "firstName": first_name}
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