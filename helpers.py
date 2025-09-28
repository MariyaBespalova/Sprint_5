import string
import random

def generate_random_email(length=10, domain="yandex.ru"):  #  генерация рандомного Email
        letters_and_digits = string.ascii_lowercase + string.digits
        random_str = ''.join(random.choice(letters_and_digits) for _ in range(length))
        email = f"{random_str}@{domain}"
        return email