import pytest
from appium import webdriver
from src.mobile.utils.R import R


desired_caps_MFP = {
    "appium:platform": f"{R.DRIVER_CONFIG.read_config_value('android', 'platform')}",
    "platformName": f"{R.DRIVER_CONFIG.read_config_value('android', 'platformName')}",
    "appium:appPackage": f"{R.DRIVER_CONFIG.read_config_value('android', 'appPackage')}",
    "appium:udid": f"{R.DRIVER_CONFIG.read_config_value('android', 'udid')}",
    "appium:app": f"{R.DRIVER_CONFIG.read_config_value('android', 'app')}",
    "appium:deviceName": f"{R.DRIVER_CONFIG.read_config_value('android', 'deviceName')}",
    "appium:automationName": f"{R.DRIVER_CONFIG.read_config_value('android', 'automationName')}"
}


@pytest.fixture(scope='function')
def mobile_driver():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps_MFP)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
