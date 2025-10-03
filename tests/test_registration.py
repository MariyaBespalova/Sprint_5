import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_random_email

class TestRegistration:
    
    def test_registration_exists(self, driver):  # проверка успешной регистрации
        driver.get(Data.REGISTRATION_URL)

        random_email = generate_random_email()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.NAME))
        driver.find_element(*Locators.EMAIL).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.VALID_PASSWORD)

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        element = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        assert element.is_displayed()
    
    def test_incorrect_password(self, driver):    #  проверка ошибки некорректного пароля
        driver.get(Data.REGISTRATION_URL)

        random_email = generate_random_email()

        driver.find_element(*Locators.NAME).send_keys(Data.VALID_NAME)
        driver.find_element(*Locators.EMAIL).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD).send_keys(Data.INVALID_PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        error_element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_ERROR_PASSWORD))
        error_text = error_element.text
        assert 'Некорректный пароль' in error_text
