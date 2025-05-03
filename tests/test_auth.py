import pytest
import allure
from pages.auth_page import AuthPage
from helpers import generate_random_email, generate_random_password, generate_random_name
from conftest import create_user

class TestAuth:

    @allure.title("Успешная регистрация уникального пользователя")
    def test_register_unique_user_success(self):
        response = AuthPage.register_user(generate_random_email(), generate_random_password(), generate_random_name())

        assert response.status_code == 200

        response_json = response.json()
        assert response_json["success"] is True
        assert "accessToken" in response_json  # Проверка наличия токена

    @allure.title("Регистрация уже существующего пользователя - ошибка")
    def test_register_existing_user_fails(self, create_user):
        response = AuthPage.register_user(create_user["email"], create_user["password"], create_user["name"])

        assert response.status_code == 403

        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "User already exists"

    @allure.title("Регистрация пользователя с отсутствующими полями - ошибка")
    def test_register_user_missing_fields(self):
        response = AuthPage.register_user("", "password123", "TestName")

        assert response.status_code == 403

        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "Email, password and name are required fields"

    @allure.title("Успешный вход пользователя")
    def test_login_success(self, create_user):
        response = AuthPage.login_user(create_user["email"], create_user["password"])

        assert response.status_code == 200

        response_json = response.json()
        assert response_json["success"] is True
        assert "accessToken" in response_json  # Проверка наличия токена
        assert "refreshToken" in response_json  # Проверка наличия refreshToken

    @allure.title("Вход с неправильными данными - ошибка")
    def test_login_wrong_credentials(self):
        response = AuthPage.login_user("wrong_email@yandex.ru", "wrongpassword")

        assert response.status_code == 401

        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "email or password are incorrect"
