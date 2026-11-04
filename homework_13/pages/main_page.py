from homework_13.pages.add_remove_page import AddRemovePage
from homework_13.pages.base_page import BasePage
from homework_13.pages.checkboxes_page import Checkboxes
from homework_13.pages.data_tables_pages import DataTablePage
from homework_13.pages.dropdown_page import DropdownPage
from homework_13.pages.hovers_page import HoversPage
from homework_13.pages.inputs_page import InputsPage
from homework_13.pages.notification_message_page import NotificationMessagePage
from homework_13.pages.typos_page import TyposPage


class MainPage(BasePage):

    @property
    def title(self):
        return self.xpath("//h1")

    @property
    def tab_add_remove_elements(self):
        return self.xpath("//a[text() = 'Add/Remove Elements']")

    @property
    def tab_checkboxes(self):
        return self.xpath("//a[text() = 'Checkboxes']")

    @property
    def tab_dropdown(self):
        return self.xpath("//a[text() = 'Dropdown']")

    @property
    def tab_inputs(self):
        return self.xpath("//a[text() = 'Inputs']")

    @property
    def tab_notification_messages(self):
        return self.xpath("//a[text() = 'Notification Messages']")

    @property
    def tab_typos(self):
        return self.xpath("//a[text() = 'Typos']")

    @property
    def tab_hovers(self):
        return self.xpath("//a[text() = 'Hovers']")

    @property
    def tab_data_table(self):
        return self.xpath("//a[text() = 'Sortable Data Tables']")

    def open_page(self, url):
        self.open(url)
        self.check_open_page()
        return self

    def check_open_page(self):
        assert self.title.text == "Welcome to the-internet", \
            "Заголовок страницы не сходится"
        return self

    def move_add_remove_elements(self):
        self.tab_add_remove_elements.click()
        return AddRemovePage(self.driver).check_open_page()

    def move_checkboxes(self):
        self.tab_checkboxes.click()
        return Checkboxes(self.driver).check_open_page()

    def move_dropdown(self):
        self.tab_dropdown.click()
        return DropdownPage(self.driver).check_open_page()

    def move_inputs(self):
        self.tab_inputs.click()
        return InputsPage(self.driver).check_title()

    def move_typos(self):
        self.tab_typos.click()
        return TyposPage(self.driver).check_open_page()

    def move_notification_messages(self):
        self.tab_notification_messages.click()
        return NotificationMessagePage(self.driver).check_open_page()

    def move_hovers(self):
        self.tab_hovers.click()
        return HoversPage(self.driver).check_open_page()

    def move_data_table(self):
        self.tab_data_table.click()
        return DataTablePage(self.driver).check_open_page()
