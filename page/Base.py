from playwright.sync_api import TimeoutError as TError
from playwright.sync_api import Page


class BasePage(object):
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.wait_for_selector(locator).click()

    def check(self, locator: str):
        self.page.check(locator)

    def uncheck(self, locator: str):
        self.page.uncheck(locator)

    def hover(self, locator: str):
        self.page.hover(locator)

    def go_to_url(self, url: str):
        self.page.goto(url)

    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)

    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except TError:
            return False

    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except TError:
            return False

    def upload(self, locator: str, files: str) -> bool:
        try:
            self.page.set_input_files(locator, files)
            return True
        except TError:
            return False

    def is_not_clickable(self, locator: str) -> bool:
        try:
            self.page.is_enabled(locator)
            return True
        except TError:
            return False

    def is_clickable(self, locator: str) -> bool:
        try:
            self.page.is_enabled(locator)
            return False
        except TError:
            return True

    def get_text(self, locator: str):
        return self.page.inner_text(locator)
