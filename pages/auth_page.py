import requests
from locators.endpoints import REGISTER_USER, LOGIN_USER, USER_DATA

class AuthPage:

    @staticmethod
    def register_user(email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return requests.post(REGISTER_USER, json=payload)

    @staticmethod
    def login_user(email, password):
        payload = {"email": email, "password": password}
        return requests.post(LOGIN_USER, json=payload)

    @staticmethod
    def get_user_data(token):
        headers = {"Authorization": token}
        return requests.get(USER_DATA, headers=headers)

    @staticmethod
    def update_user_data(token, new_data):
        headers = {"Authorization": token}
        return requests.patch(USER_DATA, headers=headers, json=new_data)
