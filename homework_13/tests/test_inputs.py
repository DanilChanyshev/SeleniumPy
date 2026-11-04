import pytest

from homework_13.pages.main_page import MainPage


class TestInputs:

    @pytest.mark.basic
    def test_inputs(self, start_ui):
        main_page = MainPage(start_ui)

        (
            main_page.move_inputs()
                .input_not_valid_date("Enter a date")
                .input_not_valid_date("%^")
                .send_keys(3)
                .arrow_up()
                .arrow_up()
                .arrow_up()
                .arrow_down()
                .arrow_down()
                .arrow_down()
        )
