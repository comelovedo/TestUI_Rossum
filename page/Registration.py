from page.Base import BasePage
from page.Locators.registration_locators import Login_Locators


class Login_Page(BasePage):
    def login_valid_account(self):
        self.type(Login_Locators.NAME_INPUT, 'Danil_Borisov@rossum.ai')
        self.type(Login_Locators.PASS_INPUT, 'Creative42435154')
        self.click(Login_Locators.SUBMIT_ACCOUNT)

    def login_invalid_account(self):
        self.type(Login_Locators.NAME_INPUT, 'Borisov_Danil@rossum.ai')
        self.type(Login_Locators.PASS_INPUT, 'Creative')
        self.click(Login_Locators.SUBMIT_ACCOUNT)

