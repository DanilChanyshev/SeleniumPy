import pytest


@pytest.fixture()
def start_ui(setup):
    setup.get("https://the-internet.herokuapp.com")
    yield setup
