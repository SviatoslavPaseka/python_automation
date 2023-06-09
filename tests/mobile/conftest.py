@pytest.fixture(scope='function')
def mobile_driver_opening_and_closing():
    driver = webdriver.Remote("http://localhost:4723/wd/hub")
    yield driver
    driver.quit()