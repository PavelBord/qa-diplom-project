from playwright.sync_api import Page
import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.boards_page import BoardsPage
from pages.tasks_page import TasksPage
from pages.dashboard_page import DashboardPage


@allure.feature("Home")
@allure.title("Отображение главной страницы")
def test_home_page(home_page: HomePage) -> None:
    with allure.step("Открыть главную страницу"):
        home_page.open()
    with allure.step("Проверить главную страницу"):
        home_page.check_opened()


@allure.feature("Login")
@allure.title("Отображение страницы логина")
def test_login_page(login_page: LoginPage) -> None:
    with allure.step("Открыть страницу логина"):
        login_page.open()
    with allure.step("Проверить страницу логина"):
        login_page.check_opened()


@allure.feature("Dashboard")
@allure.title("Отобразитьинформацию о пользователе")
@pytest.mark.dashboard
def test_authorization(login_as_admin: Page, dashboard_page: DashboardPage) -> None:
    with allure.step("Проверить информацию о пользователе"):
        dashboard_page.check_user_info()


@allure.feature("Boards")
@allure.title("Отображение страницы всех досок")
@pytest.mark.boards
def test_boards_page(login_as_admin: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:
    with allure.step("Открыть страницу досок"):
        dashboard_page.open_boards()
    with allure.step("Проверить страницу досок"):
        boards_page.check_opened()


@allure.feature("Tasks")
@allure.title("Отображение страницы всех задач")
@pytest.mark.tasks
def test_tasks_page(login_as_admin: Page, tasks_page: TasksPage) -> None:
    with allure.step("Открыть страницу задач"):
        tasks_page.open()
    with allure.step("Проверить страницу задач"):
        tasks_page.check_opened()


@allure.feature("Logout")
@allure.title("Выход из аккаунта")
@pytest.mark.logout
def test_logout(login_as_admin: Page, dashboard_page: DashboardPage, login_page: LoginPage) -> None:
    with allure.step("Выход из аккаунта"):
        dashboard_page.logout()
    with allure.step("Проверить страницу логина"):
        login_page.check_opened()
