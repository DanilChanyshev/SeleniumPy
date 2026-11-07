import pytest


class TestAddRemoveElement:

    @pytest.mark.basic
    def test_add_remove_elements(self, setup_driver, main_page):
        (
            main_page
                .open_page()
                .move_add_remove_elements()
                .click_add_button()
                .click_add_button()
                .check_count_del(2)
                .click_delete_button()
                .check_count_del(1)
                .click_delete_button()
                .check_count_del(0)
        )
