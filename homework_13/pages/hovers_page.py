import requests

from homework_13.pages.base_page import BasePage
from homework_13.test_data.users import Users


class HoversPage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def pht_user_1(self):
        return self.xpath("//h5[text() = 'name: user1']/../..//img")

    @property
    def user_1(self):
        return self.xpath("//h5[text() = 'name: user1']/following-sibling::*")

    @property
    def pht_user_2(self):
        return self.xpath("//h5[text() = 'name: user2']/../..//img")

    @property
    def user_2(self):
        return self.xpath("//h5[text() = 'name: user2']/following-sibling::*")

    @property
    def pht_user_3(self):
        return self.xpath("//h5[text() = 'name: user3']/../..//img")

    @property
    def user_3(self):
        return self.xpath("//h5[text() = 'name: user3']/following-sibling::*")

    def open_page(self):
        self.open("/hovers")
        self.check_open_page()
        return self

    def check_open_page(self):
        assert self.title.text == "Hovers"
        return self

    def click_user(self, actual_user:Users):

        match actual_user:
            case Users.user_1:
                ph_user = self.pht_user_1
                user = self.user_1
            case Users.user_2:
                ph_user = self.pht_user_2
                user = self.user_2
            case Users.user_3:
                ph_user = self.pht_user_3
                user = self.user_3
            case _:
                raise AssertionError("Указанный пользователь не найден")

        (
            self.actions
            .move_to_element(ph_user)
            .move_to_element(user)
            .click()
            .perform()
        )

        return self

    def check_status_code(self):
        response = requests.get(self.driver.current_url)
        assert response.status_code != 404, \
            f"Ссылка вернула ошибку 404: {self.driver.current_url}"
        return self
