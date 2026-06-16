import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage
from pages.dashboard_page import DashboardPage

EMAIL: str = "admin@example.com"
PASSWORD: str = "admin123"


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture(scope="function")
def boards_page(page: Page) -> BoardsPage:
    return BoardsPage(page)


@pytest.fixture(scope="function")
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture(scope="function")
def tasks_page(page: Page) -> TasksPage:
    return TasksPage(page)


@pytest.fixture(scope="function")
def authorized_page(page: Page, login_page: LoginPage) -> Page:
    login_page.open()
    login_page.login(EMAIL, PASSWORD)
    return page
