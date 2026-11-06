import allure

from homework_13.pages.base_page import BasePage


class DataTablePage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @allure.step("Открыть страницу 'table'")
    def open_page(self):
        self.open("/tables")
        self.check_open_page()
        return self

    @allure.step("Проверить что страница открылась")
    def check_open_page(self):
        assert self.title.text == "Data Tables"
        return self