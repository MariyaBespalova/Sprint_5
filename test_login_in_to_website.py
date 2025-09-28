import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_sing_in_to_account_button(self, driver):
        driver.get(Data.STELLAR_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON))  #  вход по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_BUTTON).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.PASSWORD_BUTTON).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        assert Data.STELLAR_URL in driver.current_url


    def test_log_in_to_personal_account(self, driver):
        driver.get(Data.STELLAR_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON))  #  вход через личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_BUTTON).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.PASSWORD_BUTTON).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        assert Data.STELLAR_URL in driver.current_url


    def test_log_in_to_register_form(self, driver):  #  вход через форму регистрации 
        driver.get(Data.REGISTRATION_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_REGISTRATION_PAGE))
        driver.find_element(*Locators.LOGIN_REGISTRATION_PAGE).click()
        driver.find_element(*Locators.EMAIL_BUTTON).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.PASSWORD_BUTTON).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        assert Data.STELLAR_URL in driver.current_url


    def test_log_to_in_password_recovery(self, driver):  #  вход через форму восстановления пароля
        driver.get(Data.PASSWORD_RECOVERY_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PASSWORD_RECOVERY))
        driver.find_element(*Locators.LOGIN_BUTTON_PASSWORD_RECOVERY).click()

        email_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.EMAIL_BUTTON))
        
        password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PASSWORD_BUTTON))
        email_input.send_keys(Data.VALID_EMAIL)
        password_input.send_keys(Data.VALID_PASSWORD)
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        assert Data.STELLAR_URL in driver.current_url
