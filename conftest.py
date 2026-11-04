import pytest

from webdriver.webdriver_factory import create_driver

@pytest.fixture()
def setup():
    driver = create_driver()
    driver.implicitly_wait(4)

    yield driver

    driver.quit()