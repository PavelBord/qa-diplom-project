from playwright.sync_api import Page, Locator, expect
from core.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.brand_title: Locator = page.locator(".brand-title")
        self.brand_subtitle: Locator = page.locator(".brand-subtitle")
        self.hero_title: Locator = page.locator(".hero-title")
        self.hero_description: Locator = page.locator(".hero-description")
        self.task_management_card: Locator = page.locator(
            ".feature-card").filter(has_text="Система управления задачами")
        self.task_management_link = self.task_management_card.locator(
            ".feature-link")

    def open(self) -> None:
        self.open_url("")

    def check_opened(self) -> None:
        expect(self.brand_title).to_be_visible()
        expect(self.brand_subtitle).to_be_visible()

    def open_task_management(self) -> None:
        self.task_management_link.click()

    def check_hero_banner(self) -> None:
        expect(self.hero_title).to_be_visible()
        expect(self.hero_title).to_contain_text(
            "Web Automation Torture Lab")

        expect(self.hero_description).to_be_visible()
        expect(self.hero_description).to_contain_text(
            "Комплексная платформа для практики тестирования")

    def check_feature_card(self, card_name: str) -> None:
        card = self.page.locator(".feature-card").filter(has_text=card_name)
        expect(card).to_be_visible()

    def check_feature_cards_count(self) -> None:
        expect(self.page.locator(".feature-card")).to_have_count(4)
