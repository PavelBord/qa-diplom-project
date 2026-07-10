from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class TasksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.tasks_link: Locator = page.locator(
            '[data-qa="sidebar-tasks-link"]')
        self.tasks_title: Locator = page.locator(
            '[data-qa="tasks-page-title"]')
        self.search_input: Locator = page.locator(".tasks-search-input")
        self.tasks_table: Locator = page.locator(".admin-table")
        self.tasks_list: Locator = page.locator(".admin-table tbody tr")

        self.name_header: Locator = page.locator(
            "th").filter(has_text="Название")
        self.description_header: Locator = page.locator(
            "th").filter(has_text="Описание")
        self.status_header: Locator = page.locator(
            "th").filter(has_text="Статус")
        self.priority_header: Locator = page.locator(
            "th").filter(has_text="Приоритет")
        self.date_header: Locator = page.locator(
            "th").filter(has_text="Дата создания")
        self.actions_header: Locator = page.locator(
            "th").filter(has_text="Действия")

    def open(self) -> None:
        self.tasks_link.click()

    def check_opened(self) -> None:
        expect(self.tasks_title).to_be_visible()

    def check_tasks_table(self) -> None:
        expect(self.tasks_table).to_be_visible()

        expect(self.name_header).to_be_visible()
        expect(self.description_header).to_be_visible()
        expect(self.status_header).to_be_visible()
        expect(self.priority_header).to_be_visible()
        expect(self.date_header).to_be_visible()
        expect(self.actions_header).to_be_visible()

    def search_task(self, text: str) -> None:
        self.search_input.fill(text)

    def check_task_list_visible(self) -> None:
        expect(self.tasks_list.first).to_be_visible()

    def check_search_value(self, text: str) -> None:
        expect(self.search_input).to_have_value(text)
