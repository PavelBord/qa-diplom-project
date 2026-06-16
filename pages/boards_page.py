from playwright.sync_api import Page, expect
from core.base_page import BasePage


class BoardsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator('[data-qa="boards-page-title"]')

    def check_opened(self) -> None:
        expect(self.title).to_be_visible()
        expect(self.page.get_by_text("Создать доску")).to_be_visible()
