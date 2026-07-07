from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class BoardsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title: Locator = page.locator('[data-qa="boards-page-title"]')
        self.search_input: Locator = page.locator(".boards-search-input")
        self.public_only_checkbox: Locator = page.locator(
            '[data-qa="boards-public-only-checkbox"]')
        self.boards_table: Locator = page.locator(".admin-table")
        self.name_header: Locator = page.locator(
            "th").filter(has_text="Название")
        self.description_header: Locator = page.locator(
            "th").filter(has_text="Описание")
        self.public_header: Locator = page.locator(
            "th").filter(has_text="Публичная")
        self.archived_header = page.locator(
            "th").filter(has_text="Архивирована")
        self.created_header = page.locator(
            "th").filter(has_text="Дата создания")
        self.actions_header = page.locator("th").filter(has_text="Действия")
        self.first_open_board_link = page.get_by_role(
            "link", name="Открыть").first
        self.create_task_button = page.get_by_role(
            "button", name="Создать задачу")
        self.create_board_button: Locator = page.get_by_text("Создать доску")

    def check_opened(self) -> None:
        expect(self.title).to_be_visible()
        expect(self.create_board_button).to_be_visible()

    def search_board(self, text: str) -> None:
        self.search_input.fill(text)

    def open_first_board(self) -> None:
        self.first_open_board_link.click()

    def check_board_opened(self) -> None:
        expect(self.create_task_button).to_be_visible()

    def check_boards_table(self) -> None:
        expect(self.boards_table).to_be_visible()
        expect(self.name_header).to_be_visible()
        expect(self.description_header).to_be_visible()
        expect(self.public_header).to_be_visible()
        expect(self.archived_header).to_be_visible()
        expect(self.created_header).to_be_visible()
        expect(self.actions_header).to_be_visible()

    def check_search_value(self, text: str) -> None:
        expect(self.search_input).to_have_value(text)

    def check_public_only_checkbox_visible(self) -> None:
        expect(self.public_only_checkbox).to_be_visible()

    def click_public_only_checkbox(self) -> None:
        self.public_only_checkbox.click()

    def check_public_only_checkbox_checked(self) -> None:
        expect(self.public_only_checkbox).to_be_checked()
