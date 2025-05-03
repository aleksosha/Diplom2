import random
import string

def generate_random_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@yandex.ru"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=6))
