import logging
import pytest


from enums.burger_menu_items import BurgerButton
from enums.field_name import FieldName
from enums.product_sorting import ProductSorting
from enums.products import Product
from pages.burger_menu import BurgerMenu
from pages.cart_page import CartPage
from pages.checkput_step_one_page import CheckoutStepOne
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


def test_burger_button(driver_opening_and_closing):
    USERNAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"

    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[LOGIN PAGE] is not opened"

    inventory_page: InventoryPage = login_page.login(USERNAME, PASSWORD)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.open_burger_menu()
    burger_menu = BurgerMenu(driver)
    assert burger_menu.is_opened(), "[BURGER MENU] is not opened"

    burger_menu.click_on_burger_menu_item(BurgerButton.LOGOUT)
    assert login_page.is_opened(), "[LOGIN PAGE] is not opened"

    login_page.login(USERNAME, PASSWORD)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.open_burger_menu()
    burger_menu.close_burger_menu()


def test_cart_page(driver_opening_and_closing):
    USERNAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"

    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[LOGIN PAGE] is not opened"

    inventory_page: InventoryPage = login_page.login(USERNAME, PASSWORD)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.click_add_to_cart_button(Product.SAUCE_LABS_BACKPACK)

    inventory_page.open_cart_page()

    cart_page = CartPage(driver)
    assert cart_page.is_opened(), "[CART PAGE] is not opened"

    assert cart_page.get_product_price(Product.SAUCE_LABS_BACKPACK) == 29.99

    cart_page.click_remove_product_button(Product.SAUCE_LABS_BACKPACK)

    cart_page.click_continue_to_shopping()

    # inventory_page = InventoryPage(driver)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.open_cart_page()

    assert cart_page.is_opened(), "[CART PAGE] is not opened"

    assert not cart_page.is_product_present(Product.SAUCE_LABS_BACKPACK), \
        "[CART PAGE] product present after removing from cart"


def test_product_page(driver_opening_and_closing):
    USERNAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"

    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[LOGIN PAGE] is not opened"

    inventory_page: InventoryPage = login_page.login(USERNAME, PASSWORD)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.click_product_by_name(Product.TEST_ALL_THE_THING)

    product_page = ProductPage(driver, Product.TEST_ALL_THE_THING)

    assert product_page.is_opened()

    product_page.click_add_to_cart_button()  # adding

    product_page.click_remove_button()  # removing

    product_page.click_back_to_products_button()

    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.open_cart_page()

    cart_page = CartPage(driver)

    assert cart_page.is_opened(), "[CART PAGE] is not opened"

    assert not cart_page.is_product_present(Product.TEST_ALL_THE_THING), \
        f"[CART PAGE] product '{Product.TEST_ALL_THE_THING.value[1]}' present after removing from cart"


def test_sorting_products(driver_opening_and_closing):
    USERNAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"
    AL_REVERSE_SORTING: ProductSorting = ProductSorting.ALPHABET_REVERSE
    PR_REVERSE_SORTING: ProductSorting = ProductSorting.PRICE_REVERSE
    AL_SORTING: ProductSorting = ProductSorting.ALPHABET
    PR_SORTING: ProductSorting = ProductSorting.PRICE

    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[LOGIN PAGE] is not opened"

    inventory_page: InventoryPage = login_page.login(USERNAME, PASSWORD)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"
    inventory_page.click_sort_product_by_sort_options(AL_REVERSE_SORTING)

    assert inventory_page.check_active_sorting_options() == AL_REVERSE_SORTING.value[1], \
        "[INVENTORY PAGE] the selected sort option does not match the currently active option on the sort menu"
    assert inventory_page.get_list_name_products_based_on_current_sorting() \
           == sorted(inventory_page.get_list_name_products_based_on_current_sorting(), reverse=True), \
        "[INVENTORY PAGE] the is in another after sorting: " + AL_REVERSE_SORTING.value[1]

    inventory_page.click_sort_product_by_sort_options(PR_SORTING)
    assert inventory_page.check_active_sorting_options() == PR_SORTING.value[1], \
        "[INVENTORY PAGE] the selected sort option does not match the currently active option on the sort menu"
    assert inventory_page.get_list_prices_based_on_current_sorting() \
           == sorted(inventory_page.get_list_prices_based_on_current_sorting()), \
        "[INVENTORY PAGE] the is in another after sorting: " + PR_SORTING.value[1]


def test_checkout_step_one(driver_opening_and_closing):
    USERNAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"

    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[LOGIN PAGE] is not opened"

    inventory_page: InventoryPage = login_page.login(USERNAME, PASSWORD)
    assert inventory_page.is_opened(), "[INVENTORY PAGE] is not opened"

    inventory_page.click_add_to_cart_button(Product.SAUCE_LABS_BACKPACK)

    inventory_page.open_cart_page()

    cart_page = CartPage(driver)
    assert cart_page.is_opened(), "[CART PAGE] is not opened"

    cart_page.click_checkout_button()

    checkout_step_one = CheckoutStepOne(driver)

    checkout_step_one.is_opened()

    checkout_step_one.enter_all_fields("Sat", "Sot", "100200")

    checkout_step_one.click_continue_button()


