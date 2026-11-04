from selenium.webdriver import Keys

from homework_13.pages.base_page import BasePage


class InputsPage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def input(self):
        return self.css("input")

    def check_title(self):
        assert self.title.text == "Inputs"
        return self

    def send_keys(self, text):
        self.input.click()
        self.input.clear()
        self.input.send_keys(text)
        assert self.input.get_attribute("value") == str(text), \
            f"Введенный текс не соответствует оригиналу expected {text}, actual: {self.input.get_attribute('value')}"
        return self

    def arrow_up(self):
        start_position = int(self.input.get_attribute("value"))
        self.input.send_keys(Keys.ARROW_UP)
        assert self.input.get_attribute("value") == str(start_position + 1), \
            "Значение не изменилось"
        return self

    def arrow_down(self):
        start_position = int(self.input.get_attribute("value"))
        self.input.send_keys(Keys.ARROW_DOWN)
        assert self.input.get_attribute("value") == str(start_position - 1), \
            "Значение не изменилось"
        return self

    def input_not_valid_date(self, text):
        self.input.click()
        self.input.clear()
        self.input.send_keys(text)
        assert self.input.get_attribute("value") != str(text), \
            f"Введенный текс соответствует оригиналу, а должен быть пустой"
        assert not self.input.get_attribute("value")
        return self
