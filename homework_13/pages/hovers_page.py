import allure

from homework_13.pages.base_page import BasePage
from homework_13.test_data.users import Users


class HoversPage(BasePage):

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def pht_user_1(self):
        return self.xpath("//div[@class = 'figure' and .//h5[text() = 'name: user1']]//img")

    @property
    def user_1(self):
        return self.xpath("//h5[text() = 'name: user1']/following-sibling::*")

    @property
    def pht_user_2(self):
        return self.xpath("//div[@class = 'figure' and .//h5[text() = 'name: user2']]//img")

    @property
    def user_2(self):
        return self.xpath("//h5[text() = 'name: user2']/following-sibling::*")

    @property
    def pht_user_3(self):
        return self.xpath("//div[@class = 'figure' and .//h5[text() = 'name: user3']]//img")

    @property
    def user_3(self):
        return self.xpath("//h5[text() = 'name: user3']/following-sibling::*")

    @allure.step("Открыть страницу 'hovers'")
    def open_page(self):
        self.open("/hovers")
        self.check_open_page()
        return self

    @allure.step("Проверить, что страница открылась и заголовок отображается")
    def check_open_page(self):
        assert self.title.text == "Hovers"
        return self

    @allure.step("Перейти на страницу {actual_user}")
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
