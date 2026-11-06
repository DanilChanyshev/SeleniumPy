import allure

from homework_13.pages.base_page import BasePage


class DropdownPage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def dropdown(self):
        return self.css("#dropdown")

    @property
    def options(self):
        return self.lxpath("//select//option")

    def option(self, option):
        return self.xpath(f"//option[text() = '{option}']")

    @allure.step("Открыть страницу 'dropdown'")
    def open_page(self):
        self.open("/dropdown")
        self.check_open_page()
        return self

    @allure.step("Проверить, что страница открылась и заголовок отображается")
    def check_open_page(self):
        assert self.title.text == "Dropdown List", \
            "Заголовок страницы не сходится"
        return self

    @allure.step("Проверить начальную выбранную опцию")
    def check_dropdown_start(self):
        first_option = self.options[0]
        assert len(self.options) == 3, \
            f"Ожидалось 3 элемента, фактически {len(self.options)}"
        assert (first_option.is_selected() and
                first_option.text == "Please select an option"), \
            "Начальный параметр не выбран"
        return self

    @allure.step("Выбрать опцию {option}")
    def selected_option(self, option):
        self.dropdown.click()
        selected_option = self.option(option)
        selected_option.click()
        assert selected_option.is_selected(), \
            "Выбранный параметр не стал активным"
        return self
