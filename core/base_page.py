from playwright.sync_api import Page
from config import BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, path: str):
        self.page.goto(f"{BASE_URL}/{path}")
