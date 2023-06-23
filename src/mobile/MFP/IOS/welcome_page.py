from appium.webdriver import Remote

from src.mobile.MFP.common.welcome_page_base import WelcomePageBase


class WelcomePage(WelcomePageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    def click_login_button(self):
        pass

    def is_page_opened(self) -> bool:
        pass