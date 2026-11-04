from homework_13.pages.base_page import BasePage


class AddRemovePage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def add_button(self):
        return self.css("[onclick='addElement()']")

    @property
    def delete_buttons(self):
        return self.lcss("#elements button")

    def check_open_page(self):
        assert self.title.text == "Add/Remove Elements", \
            "Заголовок страницы не сходится"
        return self

    def click_add_button(self):
        self.add_button.click()
        return self

    def check_count_del(self, count_del):
        assert count_del == len(self.delete_buttons), \
            f"Ожидалось {count_del} элементов, найдено {len(self.delete_buttons)}"
        return self

    def click_delete_button(self):
        self.delete_buttons[0].click()
        return self
