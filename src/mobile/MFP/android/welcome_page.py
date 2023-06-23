from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.MFP.common.login_page_base import LoginPageBase
from src.mobile.MFP.common.welcome_page_base import WelcomePageBase
from src.mobile.utils import initializer


class WelcomePage(WelcomePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__login_button = (AppiumBy.ID, "com.myfitnesspal.android:id/buttonLogIn")

    def click_login_button_welcome_page(self):
        self.driver.find_element(*self.__login_button).click()
        return initializer.init_page(self.driver, LoginPageBase)

    def is_page_opened(self) -> bool:
        return self.driver.find_element(*self.__login_button).is_displayed()
