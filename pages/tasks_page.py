from playwright.sync_api import Page, expect
from core.base_page import BasePage


class TasksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> None:
        self.page.locator('[data-qa="sidebar-tasks-link"]').click()

    def check_opened(self) -> None:
        expect(self.page.locator('[data-qa="tasks-page-title"]')).to_be_visible()
