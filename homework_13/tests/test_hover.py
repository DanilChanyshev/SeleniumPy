
import pytest

from homework_13.test_data.users import Users


class TestHover:

    @pytest.mark.basic
    @pytest.mark.xfail()
    def test_hover(self, setup_driver, main_page):
        (
            main_page
                .open_page()
                .move_hovers()
                .click_user(Users.user_3)
                .check_status_code()
                .go_back()
                .check_open_page()
                .click_user(Users.user_2)
                .check_status_code()
                .go_back()
                .check_open_page()
                .click_user(Users.user_1)
                .check_status_code()
                .go_back()
                .check_open_page()
        )