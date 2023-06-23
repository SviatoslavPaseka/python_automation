import abc

from src.mobile.abstract_page import AbstractPage
from appium.webdriver import Remote


class MoreMenuPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def click_on_menu_button(self, buttonsInMoreMenu):
        return

    def is_menu_button_present(self, buttonsInMoreMenu):
        return

