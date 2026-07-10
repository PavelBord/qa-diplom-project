from playwright.sync_api import Page, expect
from core.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def check_opened(self) -> None:
        expect(self.page.get_by_text("Панель управления")).to_be_visible()
        expect(self.page.get_by_text("Главная")).to_be_visible()
        expect(self.page.get_by_text("Все доски")).to_be_visible()
        expect(self.page.get_by_text("Все задачи")).to_be_visible()
        expect(self.page.get_by_text("Административная панель")).to_be_visible()

    def check_user_info(self) -> None:
        expect(self.page.get_by_role("button", name="admin")).to_be_visible()

    def open_boards(self) -> None:
        self.page.get_by_text("Все доски").click()

    def logout(self) -> None:
        self.page.get_by_role("button", name="admin").click()
        self.page.locator('[data-qa="header-logout-button"]').click()
