from homework_13.pages.base_page import BasePage


class TyposPage(BasePage):
    PASS_MESSAGE = "Sometimes you'll see a typo, other times you won't."

    @property
    def title(self):
        return self.xpath("//h3")

    @property
    def actual_text(self):
        return self.lxpath("//p")[1]

    def open_page(self):
        self.open("/typos")
        self.check_open_page()
        return self

    def check_open_page(self):
        assert self.title.text == "Typos",\
            "Заголовок не сходится"
        return self

    def check_text_in_page(self):
        count = 0
        while True:
            if self.actual_text.text == self.PASS_MESSAGE:
                print(f"Количество перезагрузок страницы: {count}")
                break
            count += 1
            self.refresh()
        return self