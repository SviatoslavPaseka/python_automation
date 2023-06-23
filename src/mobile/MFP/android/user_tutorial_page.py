from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.mobile.MFP.common.dashboard_page_base import DashboardPageBase
from src.mobile.MFP.common.user_tutorial_page_base import UserTutorialPageBase
from src.mobile.utils import initializer


class UserTutorialPage(UserTutorialPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__close_button = (
            AppiumBy.XPATH, "//*[@resource-id = 'buttonExistingUserTutorial']/child::android.widget.Button")

    def click_close_button(self):
        self.driver.find_element(*self.__close_button).click()
        return initializer.init_page(self.driver, base_class=DashboardPageBase)

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.__close_button))
