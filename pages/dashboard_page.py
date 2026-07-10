from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_title: Locator = page.get_by_text("Панель управления")
        self.home_link: Locator = page.get_by_text("Главная")
        self.boards_link: Locator = page.get_by_text("Все доски")
        self.tasks_link: Locator = page.get_by_text("Все задачи")
        self.admin_panel_text: Locator = page.get_by_text(
            "Административная панель")
        self.admin_button: Locator = page.get_by_role("button", name="admin")
        self.logout_button: Locator = page.locator(
            '[data-qa="header-logout-button"]')
        self.empty_state_title: Locator = page.locator(".empty-state-title")
        self.empty_state_message: Locator = page.locator(
            ".empty-state-message")

    def check_opened(self) -> None:
        expect(self.dashboard_title).to_be_visible()
        expect(self.home_link).to_be_visible()
        expect(self.boards_link).to_be_visible()
        expect(self.tasks_link).to_be_visible()
        expect(self.admin_panel_text).to_be_visible()

    def check_user_info(self) -> None:
        expect(self.admin_button).to_be_visible()

    def check_empty_state(self) -> None:
        expect(self.empty_state_title).to_be_visible()
        expect(self.empty_state_title).to_have_text(
            "Нет недавно открытых досок")

        expect(self.empty_state_message).to_be_visible()
        expect(self.empty_state_message).to_have_text(
            "Откройте доску, чтобы она появилась здесь")

    def open_boards(self) -> None:
        self.boards_link.click()

    def logout(self) -> None:
        self.admin_button.click()
        self.logout_button.click()
