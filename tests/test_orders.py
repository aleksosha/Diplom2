import pytest
from pages.order_page import OrderPage

class TestOrders:

    def test_create_order_authorized(self, create_user):
        ingredients = OrderPage.get_ingredients().json()["data"]
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients[:2]]
        response = OrderPage.create_order(create_user["token"], ingredient_ids)
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_order_unauthorized(self):
        ingredients = OrderPage.get_ingredients().json()["data"]
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients[:2]]
        response = OrderPage.create_order(None, ingredient_ids)
        assert response.status_code == 200  # возможно, API всё равно позволяет без токена

    def test_create_order_without_ingredients(self, create_user):
        response = OrderPage.create_order(create_user["token"], [])
        assert response.status_code == 400

    def test_create_order_invalid_ingredient_hash(self, create_user):
        response = OrderPage.create_order(create_user["token"], ["invalid_id"])
        assert response.status_code == 500

    def test_get_user_orders_authorized(self, create_user):
        response = OrderPage.get_user_orders(create_user["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_get_user_orders_unauthorized(self):
        response = OrderPage.get_user_orders("")
        assert response.status_code == 401
