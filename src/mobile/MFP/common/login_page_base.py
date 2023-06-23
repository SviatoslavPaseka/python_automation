import abc

from src.mobile.abstract_page import AbstractPage
from appium.webdriver import Remote


class LoginPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def type_email_password(self, email, password):
        return

    @abc.abstractmethod
    def click_login_button(self):
        return

    @abc.abstractmethod
    def is_login_button_enabled(self) -> bool:
        return
