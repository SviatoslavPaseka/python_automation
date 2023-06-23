from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.MFP.common.bottom_nav_bar_base import BottomNavBarBase
from src.mobile.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from selenium.webdriver.support import expected_conditions as EC

from src.mobile.utils import initializer


class BottomNavBar(BottomNavBarBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__nav_bar_item = None
        self.__bar_container = (AppiumBy.ID, "com.myfitnesspal.android:id/bottomNavigationBar")

    def click_on_nav_bar_item(self, nav_bar_item: BottomNavBarItem):
        self.__nav_bar_item = \
            (AppiumBy.ID, "com.myfitnesspal.android:id/action_{}".format(nav_bar_item.get_button_name().lower()))

        self.driver.find_element(*self.__nav_bar_item).click()
        return initializer.init_page(self.driver, nav_bar_item.get_base_class())

    def is_nav_bar_item_clickable(self, nav_bar_item: BottomNavBarItem) -> bool:
        self.__nav_bar_item = (AppiumBy.ID, "com.myfitnesspal.android:id/action_{}".format(
            nav_bar_item.get_button_name().lower()
        ))
        return self.driver.find_element(*self.__nav_bar_item).is_enabled()

    def is_present(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__bar_container))
