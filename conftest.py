import pytest
from pages.auth_page import AuthPage
from helpers import generate_random_email, generate_random_password, generate_random_name

@pytest.fixture
def create_user():
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()
    response = AuthPage.register_user(email, password, name)
    token = response.json()["accessToken"]
    return {"email": email, "password": password, "name": name, "token": token}
