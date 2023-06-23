import abc

from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.MFP.common.bottom_nav_bar_base import BottomNavBarBase
from src.mobile.MFP.common.mfp_common_page_base import MfpCommonPageBase
from selenium.webdriver.support import expected_conditions as EC

from src.mobile.MFP.common.welcome_page_base import WelcomePageBase
from src.mobile.utils import initializer
from src.mobile.utils.R import R


class MfpCommonPage(MfpCommonPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    def is_page_opened(self) -> bool:
        return super().is_page_opened()

    def wait_until_spinner_rounding(self):
        return WebDriverWait(self.driver, 30) \
            .until(EC.invisibility_of_element_located((AppiumBy.ID, "com.myfitnesspal.android:id/progressPleaseWait")))

    def get_bottom_nav_bar(self):
        bottom_nav_bar = initializer.init_page(self.driver, BottomNavBarBase)
        print(type(bottom_nav_bar))
        print("is nav bar present:" + bottom_nav_bar.is_present().__str__())

        if bottom_nav_bar.is_present():
            return bottom_nav_bar
        else:
            raise NoSuchElementException("[MFP Common Page] Bottom Nav Bar is not present!")

    def login(self, driver, email, password):
        welcome_page = initializer.init_page(self.driver, WelcomePageBase)
        assert welcome_page.is_page_opened(), "[WELCOME PAGE] is not opened"

        login_page = welcome_page.click_login_button_welcome_page()

        assert login_page.is_page_opened(), "[LOGIN PAGE] is not opened"

        login_page.type_email_password(email, password)
        assert login_page.is_login_button_enabled(), "[LOGIN PAGE] login button is not enabled after typing email and " \
                                                     "password"
        user_tutorial_page = login_page.click_login_button()

        assert user_tutorial_page.is_page_opened(), "[USER TUTORIAL WINDOW] is not opened"

        return user_tutorial_page.click_close_button()

    def default_login(self, driver):
        return self.login(driver=driver, email=R.TESTDATA.read_config_value('mfp', 'email'),
                   password=R.TESTDATA.read_config_value('mfp', 'password'))
