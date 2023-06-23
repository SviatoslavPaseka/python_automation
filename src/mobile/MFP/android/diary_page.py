from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.mobile.MFP.common.bottom_nav_bar_base import BottomNavBarBase
from src.mobile.MFP.common.diary_page_base import DiaryPageBase
from src.mobile.MFP.common.more_menu_page_base import MoreMenuPageBase
from src.mobile.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.MFP.enums.name_of_meal_diary import NameMealDiary
from src.mobile.utils import initializer


class DiaryPage(DiaryPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__more_menu_button = None
        self.__title = (
            AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']/android.widget.TextView")

    def click_more_menu_by_name(self, name_of_meal_diary: NameMealDiary) -> MoreMenuPageBase:
        self.__more_menu_button = (AppiumBy.XPATH, "//*[@text = '{}']/parent::*/parent::*/following-sibling::*[1]"
                                                   "/descendant::*/*[@resource-id = "
                                                   "'com.myfitnesspal.android:id/more']".format(
            name_of_meal_diary.get_diary_name()))

        self.driver.find_element(*self.__more_menu_button).click()
        return initializer.init_page(self.driver, MoreMenuPageBase)

    def is_more_menu_by_name_present(self, name_of_meal_diary):
        self.__more_menu_button = (AppiumBy.XPATH, "//*[@text = '{}']/parent::*/parent::*/following-sibling::*[1]"
                                                   "/descendant::*/*[@resource-id = "
                                                   "'com.myfitnesspal.android:id/more']".format(
            name_of_meal_diary.get_diary_name()))

        return self.driver.find_element(*self.__more_menu_button).is_displayed()

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.__title)) \
            and initializer.init_page(self.driver, BottomNavBarBase).is_nav_bar_item_clickable(BottomNavBarItem.DIARY)
