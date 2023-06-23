import abc
from appium.webdriver import Remote

from src.mobile.MFP.enums.nutrient_quick_add import NutrientQuickAdd
from src.mobile.abstract_page import AbstractPage


class QuickAddPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def input_nutrient(self, nutrient_name: NutrientQuickAdd, value):
        return

    @abc.abstractmethod
    def get_calories(self) -> int:
        return
