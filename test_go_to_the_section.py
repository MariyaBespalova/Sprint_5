import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_data = [
    ("Соусы", Locators.SAUCE_HEADLINE, Locators.SAUCE_SPICY),
    ("Начинки", Locators.TOPPINGS_HEADLINE, Locators.TOPPINGS_MEAT),
    ("Булки", Locators.ROLLS_HEADLINE, Locators.BURGER_INGREDIENT),
]
@pytest.mark.parametrize("section_name, section_locator, expected_element_locator", test_data)
class TestSection:
    def test_navigation(self, driver, section_name, section_locator, expected_element_locator):  
        driver.get(Data.STELLAR_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(section_locator))
        driver.find_element(*section_locator).click() 
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(expected_element_locator))
        assert element.is_displayed(), f"{section_name} раздел не отображается"
