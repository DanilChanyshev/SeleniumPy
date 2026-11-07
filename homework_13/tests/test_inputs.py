import pytest

class TestInputs:

    @pytest.mark.basic
    def test_inputs(self, setup_driver, main_page):
        (
            main_page
                .open_page()
                .move_inputs()
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
