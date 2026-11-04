
import pytest

from homework_13.pages.hovers_page import HoversPage
from homework_13.pages.main_page import MainPage
from homework_13.test_data.users import Users


class TestHover:

    @pytest.mark.basic
    @pytest.mark.xfail()
    def test_hover(self, start_ui):
        main_page = MainPage(start_ui)
        hover_page = HoversPage(start_ui)

        (
            main_page
                .move_hovers()
                .click_user(Users.user_3)
                .check_status_code()
                .go_back()
        )
        (
            hover_page
                .check_open_page()
                .click_user(Users.user_2)
                .go_back()
        )
        (
            hover_page
                .check_open_page()
                .click_user(Users.user_1)
                .go_back()
        )