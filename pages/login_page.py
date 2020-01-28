from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        substring_login = 'login'
        assert substring_login in url, f"expected '{substring_login}' to be substring of '{url}'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "Stepik228GTgt"
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        input_email.send_keys(email)
        input_password.send_keys(password)
        confirm_password.send_keys(password)
        reg_button.click()



