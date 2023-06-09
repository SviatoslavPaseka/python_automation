from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from src.web_ui.enums.products import Product
from src.web_ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(URL)
        self.continue_shopping_button = None
        self.checkout_button = None
        self.product_name = None
        self.remove_product_button = None

    def is_opened(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "continue-shopping")))
        self.continue_shopping_button = self.driver.find_element(*self.CONTINUE_SHOPPING)
        self.checkout_button = self.driver.find_element(*self.CHECKOUT)
        return self.checkout_button.is_displayed() and self.continue_shopping_button.is_displayed()

    def get_product_name(self, product: Product):
        self.product_name = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{product.value[1]}')]")
        return self.product_name.text

    def get_product_price(self, product: Product):
        product_price = self.driver.find_element(By.XPATH,
                                                 f"//div[text()='{product.value[1]}']/../following-sibling::div/div")
        # assert product_price, f"[Cart Page] Price for product named {product.value[1]} is not present!"
        tmp_price = product_price.text[1:]
        return float(tmp_price)

    def click_remove_product_button(self, product: Product):
        self.remove_product_button = self.driver.find_element(By.ID, "remove-" + product.value[0])
        self.remove_product_button.click()

    def click_continue_to_shopping(self):
        self.continue_shopping_button.click()

    def click_checkout_button(self):
        self.checkout_button.click()

    def is_product_present(self, product: Product):
        try:
            self.driver.find_element(By.XPATH, f"//div[contains(text(), '{product.value[1]}')]")
        except NoSuchElementException:
            return False
        return True
        # if self.driver.find_elements(By.CSS_SELECTOR, "div.cart_item"):
        #     return True
        # else:
        #     return False
