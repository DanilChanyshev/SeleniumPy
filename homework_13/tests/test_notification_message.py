import pytest

from homework_13.pages.main_page import MainPage


class TestNotificationMessage:

    @pytest.mark.basic
    def test_notification_message(self, start_ui):

        main_page = MainPage(start_ui)

        (
            main_page
                .move_notification_messages()
                .close_message()
                .click_new_message()
                .check_flash_message()
        )