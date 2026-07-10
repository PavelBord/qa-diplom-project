from playwright.sync_api import Page, Locator
from core.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input: Locator = page.locator("#id-input-login-email-input")
        self.password_input: Locator = page.locator("#id-input-login-password-input")
        self.login_button: Locator = page.locator('[data-qa="login-submit-button"]')

    def open(self) -> None:
        self.open_url("http://localhost:3000/login")

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
