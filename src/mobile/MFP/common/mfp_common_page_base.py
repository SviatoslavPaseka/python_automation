import abc
from appium.webdriver import Remote
from src.mobile.abstract_page import AbstractPage


class MfpCommonPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def wait_until_spinner_rounding(self):
        return

    @abc.abstractmethod
    def get_bottom_nav_bar(self):
        return

    @abc.abstractmethod
    def login(self, driver, email, password):
        return

    @abc.abstractmethod
    def default_login(self, driver):
        return
