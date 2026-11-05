from homework_13.pages.base_page import BasePage


class DataTablePage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    def open_page(self):
        self.open("/tables")
        self.check_open_page()
        return self

    def check_open_page(self):
        assert self.title.text == "Data Tables"
        return self