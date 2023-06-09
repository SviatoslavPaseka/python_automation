from selenium.webdriver.common.by import By

from src.web_ui.pages.base_page import BasePage
from src.web_ui.pages.inventory_page import InventoryPage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(url=URL)
        self.username_field = None
        self.password_field = None
        self.login_button = None
        self.error_message = None

    def is_opened(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        self.username_field = self.driver.find_element(*self.USER_NAME_INPUT)
        self.password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        self.login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        self.error_message = self.driver.find_element(*self.ERROR_MESSAGE)
        return self.username_field.is_displayed() and self.password_field.is_displayed()

    def login(self, username_text, password_text):

        self.username_field.send_keys(username_text)
        self.password_field.send_keys(password_text)
        self.login_button.click()

        return InventoryPage(self.driver)
