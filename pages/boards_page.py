from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class BoardsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title: Locator = page.locator('[data-qa="boards-page-title"]')
        self.create_board_button: Locator = page.get_by_text("Создать доску")

    def check_opened(self) -> None:
        expect(self.title).to_be_visible()
        expect(self.create_board_button).to_be_visible()
