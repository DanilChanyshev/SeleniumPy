import pytest

from homework_13.pages.main_page import MainPage


class TestAddRemoveElement:

    @pytest.mark.basic
    def test_add_remove_elements(self, start_ui):
        main_page = MainPage(start_ui)

        (
            main_page
                .check_open_page()
                .move_add_remove_elements()
                .click_add_button()
                .click_add_button()
                .check_count_del(2)
                .click_delete_button()
                .check_count_del(1)
                .click_delete_button()
                .check_count_del(0)
        )
