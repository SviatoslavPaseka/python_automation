from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from src.web_ui.enums.products import Product
from src.web_ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/inventory-item.html?id={0}"


class ProductPage(BasePage):
    def __init__(self, driver, product: Product):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(URL.format(product.value[2]))
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='inventory_details_name large_size']")))
        self.product_name = self.driver.find_element(By.XPATH, "//div[@class='inventory_details_name large_size']")
        self.product_price = self.driver.find_element(By.XPATH, "//div[@class='inventory_details_price']")
        self.back_to_products = self.driver.find_element(By.ID, "back-to-products")

    def is_opened(self):
        return self.product_name.is_displayed() and self.product_price.is_displayed()

    def get_product_name(self):
        return self.product_name.text

    def get_product_price(self):
        return float(self.product_price.text[1:])

    def click_back_to_products_button(self):
        self.back_to_products = self.driver.find_element(By.ID, "back-to-products")
        self.back_to_products.click()

    def click_add_to_cart_button(self):
        product_name_with_hyphen: str = self.product_name.text.lower().replace(" ", "-")
        try:
            self.driver.find_element(By.ID, "add-to-cart-" + product_name_with_hyphen).click()
        except NoSuchElementException:
            assert False, f"[PRODUCT '{self.product_name.text.upper()}' PAGE] there is no 'Add to cart button'"

    def click_remove_button(self):
        product_name_with_hyphen: str = self.product_name.text.lower().replace(" ", "-")
        try:
            self.driver.find_element(By.ID, "remove-" + product_name_with_hyphen).click()
        except NoSuchElementException:
            assert False, f"[PRODUCT '{self.product_name.text.upper()}' PAGE] there is no 'Remove' button"
