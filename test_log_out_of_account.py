import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_log_out_of_account(driver):
    driver.get(Data.LOGIN_URL)
    email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.EMAIL_BUTTON))
    
    password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PASSWORD_BUTTON))
    email_input.send_keys("Bespalovamariya3111@yandex.ru")
    password_input.send_keys("73377310")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()

    cabinet_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON))
    cabinet_button.click()
    exit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON))
    exit_button.click()
  