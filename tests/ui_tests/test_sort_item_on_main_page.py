import logging

from src.web_ui.pages.inventory_page import InventoryPage
from src.web_ui.pages.login_page import LoginPage
from src.web_ui.enums.product_sorting import ProductSorting
# from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
#
#
# logger = logging.getLogger(__name__)
# logger.addHandler(ZebrunnerHandler())
# logger.setLevel(logging.INFO)


def test_sorting_products(driver_opening_and_closing):
    USERNAME: str = "standard_user"
    PASSWORD: str = "secret_sauce"
    AL_REVERSE_SORTING: ProductSorting = ProductSorting.ALPHABET_REVERSE
    PR_REVERSE_SORTING: ProductSorting = ProductSorting.PRICE_REVERSE
    AL_SORTING: ProductSorting = ProductSorting.ALPHABET
    PR_SORTING: ProductSorting = ProductSorting.PRICE

    driver1 = driver_opening_and_closing
    login_page = LoginPage(driver1)
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
