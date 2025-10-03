import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConversion:
    def test_transfer_to_personal_account(self, driver):  #  переход по клику на личный кабинет
        driver.get(Data.STELLAR_URL)
        button_cabinet = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET_BUTTON))
        button_cabinet.click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        assert Data.LOGIN_URL in driver.current_url


    def test_conversion_to_constructor(self, driver):  # переход из личного кабинета в конструктор
        driver.get(Data.LOGIN_URL)
        constructor_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
        rolls_headline = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ROLLS_HEADLINE))
        assert Data.STELLAR_URL in driver.current_url


    def test_click_to_logotip(self, driver):  #  переход по клику на StellerBurgers
        driver.get(Data.LOGIN_URL)
        logotip_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGOTIP_STELLAR))
        logotip_button.click()
        rolls_headline = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ROLLS_HEADLINE))
        assert Data.STELLAR_URL in driver.current_url  
