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


@allure.feature("Home")
@allure.title("Переход в систему управления задачами")
@pytest.mark.home
def test_open_task_management(home_page: HomePage, login_page: LoginPage) -> None:
    with allure.step("Открыть главную страницу"):
        home_page.open()

    with allure.step("Открыть систему управления задачами"):
        home_page.open_task_management()

    with allure.step("Проверить страницу входа"):
        login_page.check_opened()


@allure.feature("Home")
@allure.title("Отображение главного баннера")
@pytest.mark.home
def test_home_hero_banner(home_page: HomePage) -> None:
    with allure.step("Открыть главную страницу"):
        home_page.open()

    with allure.step("Проверить главный баннер"):
        home_page.check_hero_banner()


@allure.feature("Home")
@allure.title("Отображение карточек категорий")
@pytest.mark.home
@pytest.mark.parametrize(
    "card_name",
    [
        "Клики и взаимодействия",
        "Карточки данных",
        "Форма подписки",
        "Система управления задачами",
    ],
)
def test_feature_cards(home_page: HomePage, card_name: str) -> None:
    with allure.step("Открыть главную страницу"):
        home_page.open()
    with allure.step(f"Проверить карточку {card_name}"):
        home_page.check_feature_card(card_name)


@allure.feature("Home")
@allure.title("Количество карточек на главной странице")
@pytest.mark.home
def test_feature_cards_count(home_page: HomePage) -> None:
    with allure.step("Открыть главную страницу"):
        home_page.open()
    with allure.step("Проверить количество карточек"):
        home_page.check_feature_cards_count()


@allure.feature("Login")
@allure.title("Отображение страницы логина")
def test_login_page(login_page: LoginPage) -> None:
    with allure.step("Открыть страницу логина"):
        login_page.open()
    with allure.step("Проверить страницу логина"):
        login_page.check_opened()


@allure.feature("Login")
@allure.title("Отображение сообщения об ошибке при неверных данных")
@pytest.mark.login
def test_login_with_invalid_data(login_page: LoginPage) -> None:
    with allure.step("Открыть страницу логина"):
        login_page.open()
    with allure.step("Ввести неверные данные"):
        login_page.login("pavel@example.com", "password135")
    with allure.step("Проверить сообщение об ошибке"):
        login_page.check_error_message()


@allure.feature("Login")
@allure.title("Отображение поля ввода email")
@pytest.mark.login
def test_email_input_visible(login_page: LoginPage) -> None:
    with allure.step("Открыть страницу логина"):
        login_page.open()
    with allure.step("Проверить видимость поля ввода email"):
        login_page.check_email_input_visible()


@allure.feature("Login")
@allure.title("Отображение поля пароля")
@pytest.mark.login
def test_password_input_visible(login_page: LoginPage) -> None:
    with allure.step("Открыть страницу логина"):
        login_page.open()
    with allure.step("Проверить поле пароля"):
        login_page.check_password_input_visible()


@allure.feature("Login")
@allure.title("Отображение кнопки входа")
@pytest.mark.login
def test_login_button_visible(login_page: LoginPage) -> None:
    with allure.step("Открыть страницу логина"):
        login_page.open()

    with allure.step("Проверить кнопку входа"):
        login_page.check_login_button_visible()


@allure.feature("Boards")
@allure.title("Отображение страницы всех досок")
@pytest.mark.boards
def test_boards_page(login_as_admin: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:
    with allure.step("Открыть страницу досок"):
        dashboard_page.open_boards()
    with allure.step("Проверить страницу досок"):
        boards_page.check_opened()


@allure.feature("Boards")
@allure.title("Отображение таблицы досок")
@pytest.mark.boards
def test_boards_table(login_as_admin: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:
    with allure.step("Открыть страницу досок"):
        dashboard_page.open_boards()

    with allure.step("Проверить отображение таблицы"):
        boards_page.check_boards_table()


@allure.feature("Boards")
@allure.title("Ввод текста в поиск досок")
@pytest.mark.boards
def test_search_input(login_as_admin: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:

    with allure.step("Открыть страницу досок"):
        dashboard_page.open_boards()

    with allure.step("Ввести текст в поиск"):
        boards_page.search_board("Board for task tests")

    with allure.step("Проверить введённый текст"):
        boards_page.check_search_value("Board for task tests")


@allure.feature("Boards")
@allure.title("Переключение фильтра Только публичные")
@pytest.mark.boards
def test_public_only_filter(login_as_admin: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:

    with allure.step("Открыть страницу досок"):
        dashboard_page.open_boards()

    with allure.step("Проверить отображение фильтра"):
        boards_page.check_public_only_checkbox_visible()

    with allure.step("Включить фильтр Только публичные"):
        boards_page.click_public_only_checkbox()

    with allure.step("Проверить, что фильтр включён"):
        boards_page.check_public_only_checkbox_checked()


@allure.feature("Boards")
@allure.title("Открытие первой доски")
@pytest.mark.boards
def test_open_first_board(login_as_admin: Page, dashboard_page: DashboardPage, boards_page: BoardsPage) -> None:
    with allure.step("Открыть страницу досок"):
        dashboard_page.open_boards()

    with allure.step("Открыть первую доску"):
        boards_page.open_first_board()

    with allure.step("Проверить страницу доски"):
        boards_page.check_board_opened()


@allure.feature("Dashboard")
@allure.title("Отобразить информацию о пользователе")
@pytest.mark.dashboard
def test_authorization(login_as_admin: Page, dashboard_page: DashboardPage) -> None:
    with allure.step("Проверить информацию о пользователе"):
        dashboard_page.check_user_info()


@allure.feature("Dashboard")
@allure.title("Отображение сообщения при отсутствии недавно открытых досок")
@pytest.mark.dashboard
def test_empty_recent_boards(login_as_admin: Page, dashboard_page: DashboardPage) -> None:
    with allure.step("Проверить сообщение об отсутствии недавно открытых досок"):
        dashboard_page.check_empty_state()


@allure.feature("Tasks")
@allure.title("Отображение страницы всех задач")
@pytest.mark.tasks
def test_tasks_page(login_as_admin: Page, tasks_page: TasksPage) -> None:
    with allure.step("Открыть страницу задач"):
        tasks_page.open()
    with allure.step("Проверить страницу задач"):
        tasks_page.check_opened()


@allure.feature("Tasks")
@allure.title("Отображение таблицы задач")
@pytest.mark.tasks
def test_tasks_table(login_as_admin: Page, tasks_page: TasksPage) -> None:
    with allure.step("Открыть страницу задач"):
        tasks_page.open()

    with allure.step("Проверить таблицу задач"):
        tasks_page.check_tasks_table()


@allure.feature("Tasks")
@allure.title("Ввод текста в поиск задач")
@pytest.mark.tasks
def test_search_task(login_as_admin: Page, tasks_page: TasksPage) -> None:
    with allure.step("Открыть страницу задач"):
        tasks_page.open()

    with allure.step("Ввести текст в поиск"):
        tasks_page.search_task("Task")

    with allure.step("Проверить введённый текст"):
        tasks_page.check_search_value("Task")


@allure.feature("Tasks")
@allure.title("Отображение задач в таблице")
@pytest.mark.tasks
def test_task_list_visible(login_as_admin: Page,tasks_page: TasksPage) -> None:
    with allure.step("Открыть страницу задач"):
        tasks_page.open()

    with allure.step("Проверить отображение задач в таблице"):
        tasks_page.check_task_list_visible()


@allure.feature("Logout")
@allure.title("Выход из аккаунта")
@pytest.mark.logout
def test_logout(login_as_admin: Page, dashboard_page: DashboardPage, login_page: LoginPage) -> None:
    with allure.step("Выход из аккаунта"):
        dashboard_page.logout()
    with allure.step("Проверить страницу логина"):
        login_page.check_opened()
