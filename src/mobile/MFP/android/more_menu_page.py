from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.MFP.common.more_menu_page_base import MoreMenuPageBase
from src.mobile.MFP.common.quick_add_page_base import QuickAddPageBase
from src.mobile.MFP.enums.buttons_in_more_menu import ButtonsInMoreMenu
from src.mobile.utils import initializer


class MoreMenuPage(MoreMenuPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__button = None
        self.__container = (AppiumBy.ID, "com.myfitnesspal.android:id/listViewList")

    def click_on_menu_button(self, buttonsInMoreMenu: ButtonsInMoreMenu):
        assert self.is_menu_button_present(buttonsInMoreMenu), \
            f"[MORE MENU] button with name {buttonsInMoreMenu.get_name_of_button()} is not present"
        self.__button = (AppiumBy.XPATH, "//*[contains(@text, '{}')]".format(buttonsInMoreMenu.get_name_of_button()))
        self.driver.find_element(*self.__button).click()
        return initializer.init_page(self.driver, QuickAddPageBase)

    def is_menu_button_present(self, buttonsInMoreMenu):
        self.__button = (AppiumBy.XPATH, "//*[contains(@text, '{}')]".format(buttonsInMoreMenu.get_name_of_button()))
        return self.driver.find_element(*self.__button).is_displayed()

    def is_page_opened(self) -> bool:
        return self.driver.find_element(*self.__container).is_displayed()
