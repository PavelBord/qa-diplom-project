from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input: Locator = page.locator("#id-input-login-email-input")
        self.password_input: Locator = page.locator("#id-input-login-password-input")
        self.login_button: Locator = page.locator('[data-qa="login-submit-button"]')
        self.error_message: Locator = page.locator(".toast-message")

    def open(self) -> None:
        self.open_url("login")

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def check_opened(self) -> None:
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()

    def check_error_message(self) -> None:
        expect(self.error_message).to_be_visible()

    def check_email_input_visible(self) -> None:
        expect(self.email_input).to_be_visible()

    def check_password_input_visible(self) -> None:
        expect(self.password_input).to_be_visible()

    def check_login_button_visible(self) -> None:
        expect(self.login_button).to_be_visible()
