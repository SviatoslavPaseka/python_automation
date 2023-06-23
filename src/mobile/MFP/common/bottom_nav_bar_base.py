import abc
from appium.webdriver import Remote

from src.mobile.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.abstract_ui_object import AbstractUIObject


class BottomNavBarBase(AbstractUIObject):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_on_nav_bar_item(self, nav_bar_item: BottomNavBarItem):
        return

    @abc.abstractmethod
    def is_nav_bar_item_clickable(self, nav_bar_item: BottomNavBarItem):
        return

    @abc.abstractmethod
    def is_present(self) -> bool:
        return
