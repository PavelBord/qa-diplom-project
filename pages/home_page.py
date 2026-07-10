from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.brand_title: Locator = page.locator(".brand-title")
        self.brand_subtitle: Locator = page.locator(".brand-subtitle")
        self.task_management_link: Locator = page.locator('a[href="/task-management"]')

    def open(self) -> None:
        self.open_url("")

    def check_opened(self) -> None:
        expect(self.brand_title).to_be_visible()
        expect(self.brand_subtitle).to_be_visible()

    def open_task_management(self) -> None:
        self.task_management_link.click()

    
