from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class TasksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.tasks_link: Locator = page.locator('[data-qa="sidebar-tasks-link"]')
        self.tasks_title: Locator = page.locator('[data-qa="tasks-page-title"]')

    def open(self) -> None:
        self.tasks_link.click()

    def check_opened(self) -> None:
        expect(self.tasks_title).to_be_visible()
