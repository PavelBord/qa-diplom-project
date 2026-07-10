from playwright.sync_api import Page


class BasePage:
    BASE_URL = "http://localhost:3000"

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url)
