import pytest


class TestNotificationMessage:

    @pytest.mark.basic
    def test_notification_message(self, setup_driver, main_page):
        (
            main_page
                .open_page()
                .move_notification_messages()
                .close_message()
                .click_new_message()
                .check_flash_message()
        )