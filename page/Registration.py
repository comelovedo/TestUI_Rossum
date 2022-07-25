from page.Base import BasePage
from page.Locators.registration_locators import Login_Locators


class Login_Page(BasePage):
    def login_valid_account(self):
        self.type(Login_Locators.NAME_INPUT, 'YourEmail')
        self.type(Login_Locators.PASS_INPUT, 'YourPassword')
        self.click(Login_Locators.SUBMIT_ACCOUNT)

    def login_invalid_account(self):
        self.type(Login_Locators.NAME_INPUT, 'YourEmail')
        self.type(Login_Locators.PASS_INPUT, 'YourPassword')
        self.click(Login_Locators.SUBMIT_ACCOUNT)

