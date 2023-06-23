import abc
from appium.webdriver import Remote


class AbstractPage:
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver:  Remote):
        self.driver = driver

    @abc.abstractmethod
    def is_page_opened(self) -> bool:
        return
