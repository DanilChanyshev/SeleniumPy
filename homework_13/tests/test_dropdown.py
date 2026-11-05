import pytest

class TestDropdown:

    @pytest.mark.basic
    def test_dropdown(self, setup_driver, main_page):
        (
            main_page
                .open_page()
                .move_dropdown()
                .check_dropdown_start()
                .selected_option("Option 1")
                .selected_option("Option 2")
        )
