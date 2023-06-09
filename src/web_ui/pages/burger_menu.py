from selenium.webdriver.common.by import By

from src.web_ui.enums.burger_menu_items import BurgerButton
from src.web_ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/inventory.html"


class BurgerMenu(BasePage):
    CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.close_button = None
        self.burger_menu_item = None

    def is_opened(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "react-burger-cross-btn")))
        self.close_button = self.driver.find_element(*self.CLOSE_BUTTON)
        return self.close_button.is_displayed()

    def close_burger_menu(self):
        self.is_opened()
        self.close_button.click()

    def click_on_burger_menu_item(self, button: BurgerButton):
        self.wait.until(EC.visibility_of_element_located((By.ID, button.value)))
        self.burger_menu_item = self.driver.find_element(By.ID, button.value)
        self.burger_menu_item.click()
