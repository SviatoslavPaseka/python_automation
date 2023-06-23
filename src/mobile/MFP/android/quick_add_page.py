from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.MFP.common.quick_add_page_base import QuickAddPageBase
from src.mobile.MFP.enums.nutrient_quick_add import NutrientQuickAdd


class QuickAddPage(QuickAddPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__nutrient_field = None
        self.__calories_value = (AppiumBy.ID, "com.myfitnesspal.android:id/tvQuickCalories")
        self.__done_button = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Done']")
        self.__title = (AppiumBy.XPATH, "//*[@text='Quick Add']")

    def input_nutrient(self, nutrient_name: NutrientQuickAdd, value):
        self.__nutrient_field = (
            AppiumBy.XPATH, "com.myfitnesspal.android:id/tvQuick{}".format(nutrient_name.get_name_in_DOM_id()))
        self.driver.find_element(*self.__nutrient_field).send_keys(value)
        self.driver.hide_keyboard()

    def get_calories(self) -> int:
        calories = self.driver.find_element(*self.__calories_value).get_attribute("text")
        try:
            return int(calories)
        except ValueError:
            raise "[QUICK ADD] invalid value"

    def is_page_opened(self) -> bool:
        return self.driver.find_element(*self.__title).is_displayed() \
            and self.driver.find_element(*self.__done_button).is_displayed()
