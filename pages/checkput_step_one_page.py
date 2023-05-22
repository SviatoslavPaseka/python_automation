from selenium.webdriver.common.by import By

from enums.field_name import FieldName
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/checkout-step-one.html"


class CheckoutStepOne(BasePage):
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(URL)
        self.input_field = None
        self.cancel_button = None
        self.continue_button = None
        self.shopping_cart_link = None
        self.burger_button = None

    def is_opened(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "continue")))
        self.cancel_button = self.driver.find_element(*self.CANCEL)
        self.continue_button = self.driver.find_element(*self.CONTINUE)
        self.shopping_cart_link = self.driver.find_element(*self.SHOPPING_CART)
        self.burger_button = self.driver.find_element(*self.BURGER_BUTTON)
        return self.cancel_button.is_displayed() and self.burger_button.is_displayed()

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_continue_button(self):
        self.continue_button.click()

    def click_shopping_cart_link(self):
        self.shopping_cart_link.click()

    def open_burger_menu(self):
        self.burger_button.click()

    def enter_value_to_input_field_by_field_name(self, field_name: FieldName, value: str):
        self.input_field = self.driver.find_element(By.ID, field_name.value)
        self.input_field.send_keys(value)

    def enter_all_fields(self, firstname, lastname, postalcode):
        self.enter_value_to_input_field_by_field_name(FieldName.FIRSTNAME, firstname)
        self.enter_value_to_input_field_by_field_name(FieldName.LASTNAME, lastname)
        self.enter_value_to_input_field_by_field_name(FieldName.POSTALCODE, postalcode)

    def _load(self):
        self.cancel_button = self.driver.find_element(*self.CANCEL)
        self.continue_button = self.driver.find_element(*self.CONTINUE)
        self.shopping_cart_link = self.driver.find_element(*self.SHOPPING_CART)
        self.burger_button = self.driver.find_element(*self.BURGER_BUTTON)
