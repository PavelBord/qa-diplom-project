from playwright.sync_api import Page, expect
from core.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> None:
        self.open_url("http://localhost:3000/automation-lab")

    def check_opened(self) -> None:
        expect(self.page.locator(".brand-title")).to_be_visible()
        expect(self.page.get_by_text("Категории")).to_be_visible()

    def open_task_management(self) -> None:
        self.page.locator('a[href="/task-management"]').click()
