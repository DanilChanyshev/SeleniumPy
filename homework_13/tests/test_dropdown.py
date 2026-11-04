import pytest

from homework_13.pages.main_page import MainPage


class TestDropdown:

    @pytest.mark.basic
    def test_dropdown(self, start_ui):
        main_page = MainPage(start_ui)

        (
            main_page.move_dropdown()
                .check_dropdown_start()
                .selected_option("Option 1")
                .selected_option("Option 2")
        )
