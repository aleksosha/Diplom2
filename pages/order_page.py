import requests
from locators.endpoints import ORDERS, INGREDIENTS

class OrderPage:

    @staticmethod
    def get_ingredients():
        return requests.get(INGREDIENTS)

    @staticmethod
    def create_order(token, ingredients):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        return requests.post(ORDERS, headers=headers, json=payload)

    @staticmethod
    def get_user_orders(token):
        headers = {"Authorization": token}
        return requests.get(ORDERS, headers=headers)
