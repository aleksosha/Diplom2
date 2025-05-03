import requests
import allure
from locators.endpoints import ORDERS, INGREDIENTS

class OrderPage:

    @staticmethod
    @allure.step("Получение списка ингредиентов")  # Шаг с описанием на русском
    def get_ingredients():
        return requests.get(INGREDIENTS)

    @staticmethod
    @allure.step("Создание заказа с ингредиентами: {ingredients}")  # Шаг с описанием на русском
    def create_order(token, ingredients):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        return requests.post(ORDERS, headers=headers, json=payload)

    @staticmethod
    @allure.step("Получение заказов пользователя с токеном: {token}")  # Шаг с описанием на русском
    def get_user_orders(token):
        headers = {"Authorization": token}
        return requests.get(ORDERS, headers=headers)
