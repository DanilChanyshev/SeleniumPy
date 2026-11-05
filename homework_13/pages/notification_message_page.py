from homework_13.pages.base_page import BasePage


class NotificationMessagePage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def button_new_message(self):
        return self.xpath("//a[text() = 'Click here']")

    @property
    def close_message_btn(self):
        return self.css(".close")

    @property
    def action_message(self):
        return self.css("#flash")

    def open_page(self):
        self.open("/notification_message_rendered")
        self.check_open_page()
        return self

    def check_open_page(self):
        assert self.title.text == "Notification Message"
        return self

    def click_new_message(self):
        self.button_new_message.click()
        self.wait_until("#flash")
        return self

    def check_flash_message(self):
        expected_message = [
            "Action unsuccesful, please try again",
            "Action successful"
        ]
        actual_message = self.action_message.text
        assert any (text in actual_message for text in expected_message),\
            f"Получено неожиданное сообщение {actual_message}"
        return self


    def close_message(self):
        self.close_message_btn.click()
        return self