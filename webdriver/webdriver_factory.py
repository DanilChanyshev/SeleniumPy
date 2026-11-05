from selenium import webdriver

from webdriver.options import create_options


def create_driver():
    options = create_options()
    driver = webdriver.Chrome(options=options)
    return driver
