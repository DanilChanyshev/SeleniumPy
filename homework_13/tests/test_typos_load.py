import pytest



class TestTypos:

    @pytest.mark.basic
    def test_typos_load(self, setup_driver, main_page):
        (
            main_page
                .open_page()
                .move_typos()
                .check_text_in_page()
        )
