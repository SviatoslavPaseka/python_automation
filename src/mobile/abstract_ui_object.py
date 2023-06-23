import abc
from appium.webdriver import Remote


class AbstractUIObject:
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver: Remote):
        self.driver = driver

    @abc.abstractmethod
    def is_present(self) -> bool:
        return
