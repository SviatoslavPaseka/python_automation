from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.MFP.common.dashboard_page_base import DashboardPageBase
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(DashboardPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__user_avatar = (AppiumBy.XPATH, "//android.view.View[@content-desc='User avatar']")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__user_avatar))

