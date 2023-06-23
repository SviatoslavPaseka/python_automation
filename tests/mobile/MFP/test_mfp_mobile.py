import time

from src.mobile.MFP.common.mfp_common_page_base import MfpCommonPageBase
from src.mobile.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.MFP.enums.buttons_in_more_menu import ButtonsInMoreMenu
from src.mobile.MFP.enums.name_of_meal_diary import NameMealDiary
from src.mobile.MFP.enums.nutrient_quick_add import NutrientQuickAdd
from src.mobile.utils import initializer


def test_calories_validation_quick_add(mobile_driver):
    driver = mobile_driver
    mfp_common_page = initializer.init_page(driver, MfpCommonPageBase)
    dashboard_page = mfp_common_page.default_login(driver)
    assert dashboard_page.is_page_opened(), "[DASHBOARD PAGE] is not opened"
    diary_page = mfp_common_page.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page.is_page_opened(), "[DIARY PAGE] is not opened"
    more_menu = diary_page.click_more_menu_by_name(NameMealDiary.BREAKFAST)
    assert more_menu.is_page_opened(), "[MORE MENU] is not opened"
    quick_add_page = more_menu.click_on_menu_button(ButtonsInMoreMenu.QUICK_ADD)
    quick_add_page.input_nutrient(NutrientQuickAdd.FAT, 10)
    quick_add_page.input_nutrient(NutrientQuickAdd.CARBS, 10)
    quick_add_page.input_nutrient(NutrientQuickAdd.PROTEIN, 10)

    assert quick_add_page.get_calories() == 170, "[QUICK ADD] amount calories is not expected"


def test_with_page_factory_implemented(mobile_driver):
    driver = mobile_driver
    mfp_common_page = initializer.init_page(driver, MfpCommonPageBase)
    mfp_common_page.default_login(driver)

    for item in BottomNavBarItem.__members__.values():
        if item == BottomNavBarItem.DASHBOARD:
            continue
        mfp_common_page.get_bottom_nav_bar().click_on_nav_bar_item(item)
        time.sleep(2)


