from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.MFP.common.login_page_base import LoginPageBase
from appium.webdriver import Remote

from src.mobile.MFP.common.user_tutorial_page_base import UserTutorialPageBase
from src.mobile.utils import initializer


class LoginPage(LoginPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__email_field = (AppiumBy.ID, "com.myfitnesspal.android:id/email_address_edit")
        self.__password_field = (AppiumBy.ID, "com.myfitnesspal.android:id/password_edit")
        self.__login_button = (AppiumBy.ID, "com.myfitnesspal.android:id/login_button")

    def type_email_password(self, email, password):
        self.driver.find_element(*self.__email_field).send_keys(email)
        self.driver.find_element(*self.__password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.__login_button).click()
        return initializer.init_page(self.driver, UserTutorialPageBase)

    def is_login_button_enabled(self) -> bool:
        return self.driver.find_element(*self.__login_button).is_enabled()

    def is_page_opened(self) -> bool:
        return self.driver.find_element(*self.__email_field).is_displayed() \
            and self.driver.find_element(*self.__password_field).is_displayed()
