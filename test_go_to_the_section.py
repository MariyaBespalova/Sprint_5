import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# переход в раздел Соусы
def test_go_to_sauses(driver):
    driver.get(Data.STELLAR_URL)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ROLLS_HEADLINE))
    driver.find_element(*Locators.SAUCE_HEADLINE).click() 
    sauce_spicy = driver.find_element(*Locators.SAUCE_SPICY)
    assert sauce_spicy.is_displayed()

#  переход в раздел Начинки
def test_go_to_toppings(driver):
    driver.get(Data.STELLAR_URL)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ROLLS_HEADLINE))
    driver.find_element(*Locators.TOPPINGS_HEADLINE).click() 
    toppings_meat = driver.find_element(*Locators.TOPPINGS_MEAT)
    assert toppings_meat.is_displayed()