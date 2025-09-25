import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#  вход по кнопке "Войти в аккаунт"
def test_sing_in_to_account_button(driver):
    driver.get(Data.STELLAR_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON))
    driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()
    sleep(3)
    driver.find_element(*Locators.EMAIL_BUTTON).send_keys('Bespalovamariya3111@yandex.ru')
    driver.find_element(*Locators.PASSWORD_BUTTON).send_keys('73377310')
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
    assert Data.STELLAR_URL in driver.current_url

#  вход через личный кабинет
def test_log_in_to_personal_account(driver):
    driver.get(Data.STELLAR_URL)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON))
    driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()
    sleep(3)
    driver.find_element(*Locators.EMAIL_BUTTON).send_keys('Bespalovamariya3111@yandex.ru')
    driver.find_element(*Locators.PASSWORD_BUTTON).send_keys('73377310')
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    sleep(3)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
    assert Data.STELLAR_URL in driver.current_url

#  вход через форму регистрации 
def test_log_in_to_register_form(driver):
    driver.get(Data.REGISTRATION_URL)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_REGISTRATION_PAGE))
    driver.find_element(*Locators.LOGIN_REGISTRATION_PAGE).click()
    driver.find_element(*Locators.EMAIL_BUTTON).send_keys('Bespalovamariya3111@yandex.ru')
    driver.find_element(*Locators.PASSWORD_BUTTON).send_keys('73377310')
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    sleep(3)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
    assert Data.STELLAR_URL in driver.current_url

#  вход через форму восстановления пароля
def test_log_to_in_password_recovery(driver):
    driver.get(Data.PASSWORD_RECOVERY_URL)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PASSWORD_RECOVERY))
    driver.find_element(*Locators.LOGIN_BUTTON_PASSWORD_RECOVERY).click()

    email_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.EMAIL_BUTTON))
    
    password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PASSWORD_BUTTON))
    email_input.send_keys("Bespalovamariya3111@yandex.ru")
    password_input.send_keys("73377310")
    login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
    assert Data.STELLAR_URL in driver.current_url