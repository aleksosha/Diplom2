import pytest
from pages.auth_page import AuthPage
from helpers import generate_random_email, generate_random_password, generate_random_name

class TestAuth:

    def test_register_unique_user_success(self):
        response = AuthPage.register_user(generate_random_email(), generate_random_password(), generate_random_name())
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_register_existing_user_fails(self, create_user):
        response = AuthPage.register_user(create_user["email"], create_user["password"], create_user["name"])
        assert response.status_code == 403

    def test_register_user_missing_fields(self):
        response = AuthPage.register_user("", "password123", "TestName")
        assert response.status_code == 403

    def test_login_success(self, create_user):
        response = AuthPage.login_user(create_user["email"], create_user["password"])
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_login_wrong_credentials(self):
        response = AuthPage.login_user("wrong_email@yandex.ru", "wrongpassword")
        assert response.status_code == 401
