import allure

from homework_13.pages.base_page import BasePage


class Checkboxes(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def checkboxes(self):
        return self.lcss("input[type='checkbox']")

    @allure.step("Открыть страницу 'checkboxes'")
    def open_page(self):
        self.open("/checkboxes")
        self.check_open_page()
        return self

    @allure.step("Проверить, что страница открылась и заголовок отображается")
    def check_open_page(self):
        assert self.title.text == "Checkboxes", \
            "Checkboxes is not open"
        return self

    @allure.step("Проверить состояние чекбокса")
    def check_selected_checkbox(self, count_box, status):
        assert self.checkboxes[count_box].is_selected() == status, "Selected checkbox is not correct"
        return self

    @allure.step("Нажать на чекбокс")
    def click_checkbox(self, count_box):
        self.checkboxes[count_box].click()
        return self
