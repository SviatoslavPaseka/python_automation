import abc
from appium.webdriver import Remote

from src.mobile.abstract_page import AbstractPage


class DiaryPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver=driver)

    @abc.abstractmethod
    def click_more_menu_by_name(self, name_of_meal_diary):
        return

    @abc.abstractmethod
    def is_more_menu_by_name_present(self, name_of_meal_diary):
        return
