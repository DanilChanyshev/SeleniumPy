from homework_13.pages.base_page import BasePage


class DataTablePage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    def check_open_page(self):
        assert self.title.text == "Data Tables"
        return self