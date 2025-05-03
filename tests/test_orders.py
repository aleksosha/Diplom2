import pytest
import allure
from pages.order_page import OrderPage
from conftest import create_user

class TestOrders:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, create_user):
        ingredients = OrderPage.get_ingredients().json()["data"]
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients[:2]]
        response = OrderPage.create_order(create_user["token"], ingredient_ids)

        assert response.status_code == 200

        response_json = response.json()
        assert response_json["success"] is True
        assert "order" in response_json
        assert "number" in response_json["order"]

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_unauthorized(self):
        ingredients = OrderPage.get_ingredients().json()["data"]
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients[:2]]
        response = OrderPage.create_order(None, ingredient_ids)

        assert response.status_code == 200

        response_json = response.json()
        assert "success" in response_json
        assert response_json["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_user):
        response = OrderPage.create_order(create_user["token"], [])

        assert response.status_code == 400

        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_ingredient_hash(self, create_user):
        response = OrderPage.create_order(create_user["token"], ["invalid_id"])

        assert response.status_code == 500

        if 'application/json' in response.headers.get('Content-Type', ''):
            response_json = response.json()
            assert response_json["success"] is False
            assert "message" in response_json
        else:
            print("Ответ от сервера не является JSON. Содержимое ответа:", response.text)
            assert "<title>Error</title>" in response.text

    @allure.title("Получение заказов пользователя, авторизованного в системе")
    def test_get_user_orders_authorized(self, create_user):
        response = OrderPage.get_user_orders(create_user["token"])

        assert response.status_code == 200

        response_json = response.json()
        assert response_json["success"] is True
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)

    @allure.title("Получение заказов пользователя без авторизации")
    def test_get_user_orders_unauthorized(self):
        response = OrderPage.get_user_orders("")

        assert response.status_code == 401

        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "You should be authorised"
