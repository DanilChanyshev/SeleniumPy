import pytest

from homework_13.pages.main_page import MainPage


@pytest.fixture()
def main_page(setup_driver):
    return MainPage(setup_driver)
