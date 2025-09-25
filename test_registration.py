import random
import string
import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def generate_random_email(length=10, domain="yandex.ru"):  #  генерация рандомного Email
    letters_and_digits = string.ascii_lowercase + string.digits
    random_str = ''.join(random.choice(letters_and_digits) for _ in range(length))
    email = f"{random_str}@{domain}"
    return email

def test_registration_exists(driver):  # проверка успешной регистрации
    driver.get(Data.REGISTRATION_URL)

    random_email = generate_random_email()
    sleep(3)
    driver.find_element(*Locators.NAME).send_keys('Mariya')
    driver.find_element(*Locators.EMAIL).send_keys(random_email)
    driver.find_element(*Locators.PASSWORD).send_keys('73377310')

    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    sleep(3)

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
    
def test_incorrect_password(driver):    #  проверка ошибки некорректного пароля
    driver.get(Data.REGISTRATION_URL)

    random_email = generate_random_email()

    driver.find_element(*Locators.NAME).send_keys('Mariya')
    driver.find_element(*Locators.EMAIL).send_keys(random_email)
    driver.find_element(*Locators.PASSWORD).send_keys('123')
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    sleep(3)

    error_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_ERROR_PASSWORD))
    error_text = error_element.text
    assert 'Некорректный пароль' in error_text