import pytest
from pages.auth_page import AuthPage
from helpers import generate_random_email, generate_random_password, generate_random_name


@pytest.fixture
def create_user(request):
    email = generate_random_email()
    password = generate_random_password()
    name = generate_random_name()

    # Регистрация пользователя
    response = AuthPage.register_user(email, password, name)
    token = response.json()["accessToken"]

    # Возвращаем данные пользователя
    user_data = {"email": email, "password": password, "name": name, "token": token}

    # Это будет выполняться после теста, чтобы удалить пользователя
    def finalize():
        AuthPage.delete_user(user_data["token"])

    # Указываем финализатор для фикстуры
    request.addfinalizer(finalize)

    return user_data
