from playwright.sync_api import Page, expect
import allure
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage
from pages.dashboard_page import DashboardPage


@allure.feature("Login")
@allure.title("Отображение страницы логина")
def test_login_page(login_page: LoginPage) -> None:
    login_page.open()

    expect(login_page.email_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


@allure.feature("Home")
@allure.title("Отображение главной страницы")
def test_home_page(home_page: HomePage) -> None:
    home_page.open()
    home_page.check_opened()


@allure.feature("Tasks")
@allure.title("Отображение страницы всех задач")
@pytest.mark.user1
def test_tasks_page(authorized_page: Page, tasks_page: TasksPage) -> None:
    tasks_page.open()
    tasks_page.check_opened()


@allure.feature("Dashboard")
@allure.title("Отображение информации о пользователе")
@pytest.mark.user2
def test_user_information(authorized_page: Page, dashboard_page: DashboardPage) -> None:
    dashboard_page.check_user_info()


@allure.feature("Boards")
@allure.title("Отображение страницы всех досок")
@pytest.mark.user3
def test_boards_page(authorized_page: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:
    dashboard_page.open_boards()
    boards_page.check_opened()


@allure.feature("Logout")
@allure.title("Выход из аккаунта")
@pytest.mark.user4
def test_logout(authorized_page: Page, dashboard_page: DashboardPage, login_page: LoginPage) -> None:
    dashboard_page.logout()
    expect(login_page.email_input).to_be_visible()
