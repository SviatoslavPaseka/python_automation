from selenium.webdriver.common.by import By

from enums.product_sorting import ProductSorting
from enums.products import Product
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.burger_menu import BurgerMenu

URL = "https://www.saucedemo.com/inventory.html"


class InventoryPage(BasePage):
    LOGO = (By.CSS_SELECTOR, ".app_logo")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(URL)
        self.logo = None
        self.shopping_cart_link = None
        self.burger_button = None
        self.add_to_cart_button = None
        self.product_sort_selector = None

    def open_burger_menu(self):
        self.burger_button.click()

    def is_opened(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))
        self.logo = self.driver.find_element(*self.LOGO)
        self.shopping_cart_link = self.driver.find_element(*self.SHOPPING_CART)
        self.burger_button = self.driver.find_element(*self.BURGER_BUTTON)
        return self.logo.is_displayed() and self.shopping_cart_link.is_displayed()

    def click_add_to_cart_button(self, product: Product):
        self.wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-" + product.value[0])))
        self.add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-" + product.value[0])
        self.add_to_cart_button.click()

    def open_cart_page(self):
        self.shopping_cart_link.click()

    def click_product_by_name(self, product: Product):
        product_name = self.driver.find_element(By.XPATH, f"//div[text()='{product.value[1]}']")
        product_name.click()

    def click_sort_product_by_sort_options(self, product_sorting: ProductSorting):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
        self.product_sort_selector = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.product_sort_selector.click()
        self.driver.find_element(By.XPATH, f"//option[@value='{product_sorting.value[0]}']").click()

    def check_active_sorting_options(self):
        return self.driver.find_element(By.CLASS_NAME, "active_option").text

    def get_list_prices_based_on_current_sorting(self) -> list:
        return [float(price_curr.text[1:]) for price_curr in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]

    def get_list_name_products_based_on_current_sorting(self) -> list:
        return [name.text for name in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
