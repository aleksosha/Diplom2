import requests
import allure
from locators.endpoints import REGISTER_USER, LOGIN_USER, USER_DATA, DELETE_USER

class AuthPage:

    @staticmethod
    @allure.step("Регистрация пользователя с email: {email}, паролем: {password}, именем: {name}")  # Аннотация с описанием шагов на русском
    def register_user(email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return requests.post(REGISTER_USER, json=payload)

    @staticmethod
    @allure.step("Вход пользователя с email: {email} и паролем: {password}")  # Аннотация с описанием шагов на русском
    def login_user(email, password):
        payload = {"email": email, "password": password}
        return requests.post(LOGIN_USER, json=payload)

    @staticmethod
    @allure.step("Получение данных пользователя с токеном: {token}")  # Аннотация с описанием шагов на русском
    def get_user_data(token):
        headers = {"Authorization": token}
        return requests.get(USER_DATA, headers=headers)

    @staticmethod
    @allure.step("Обновление данных пользователя с токеном: {token} и новыми данными: {new_data}")  # Аннотация с описанием шагов на русском
    def update_user_data(token, new_data):
        headers = {"Authorization": token}
        return requests.patch(USER_DATA, headers=headers, json=new_data)

    @staticmethod
    @allure.step("Удаление пользователя с токеном: {token}")  # Аннотация с описанием шагов на русском
    def delete_user(token):
        headers = {"Authorization": f"Bearer {token}"}  # Авторизация через Bearer Token
        response = requests.delete(DELETE_USER, headers=headers)
        return response
