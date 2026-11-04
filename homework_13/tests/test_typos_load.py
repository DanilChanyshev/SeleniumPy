import pytest

from homework_13.pages.main_page import MainPage


class TestTypos:

    @pytest.mark.basic
    def test_typos_load(self, start_ui):
        main_page = MainPage(start_ui)

        (
            main_page
                .move_typos()
                .check_text_in_page()
        )
