import pytest

from homework_13.pages.main_page import MainPage


class TestCheckboxes:

    @pytest.mark.basic
    def test_checkboxes_element(self, start_ui):
        main_page = MainPage(start_ui)

        (
            main_page.move_checkboxes()
                .check_selected_checkbox(0, False)
                .click_checkbox(0)
                .check_selected_checkbox(0, True)
                .check_selected_checkbox(1, True)
                .click_checkbox(1)
                .check_selected_checkbox(1, False)
        )
