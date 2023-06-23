import abc

from src.mobile.abstract_page import AbstractPage
from appium.webdriver import Remote


class WelcomePageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_login_button_welcome_page(self):
        return
