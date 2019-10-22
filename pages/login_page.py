from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_FIELD)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_CONFIRM_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)

        register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_REGISTER_BUTTON)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        current_url_list_without_empty_strings = [part for part in current_url.split('/') if part != '']

        assert current_url_list_without_empty_strings[-1] == 'login', "Page URL don't ends with 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            "Registration form is not presented"
