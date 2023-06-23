from src.mobile.MFP.common.welcome_page_base import WelcomePageBase
from src.mobile.utils import initializer


def test_subclass(mobile_driver):
    driver = mobile_driver
    welcome_page = initializer_util.init_page(driver, WelcomePageBase)

