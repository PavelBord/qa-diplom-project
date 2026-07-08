import pytest
import allure
from services.boards_service import BoardsService
from services.tasks_service import TasksService
from models.task_model import TaskModel


def create_board(admin_token):
    with allure.step("Создать тестовую доску"):
        board_data = {
            "title": "Board for task tests",
            "description": "Board created from API test",
            "public": True,
        }

    response = BoardsService().create_board(admin_token, board_data)

    assert response.status_code == 201

    return response.json()["id"]


@allure.feature("Tasks API")
@allure.title("Получение списка задач")
def test_get_tasks(admin_token):
    with allure.step("Создать тестовую доску"):
        board_id = create_board(admin_token)

    with allure.step("Получить список задач"):
        response = TasksService().get_tasks(board_id=board_id, token=admin_token)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить структуру данных"):
        tasks = response.json()

    if tasks:
        TaskModel(**tasks[0])


@allure.feature("Tasks API")
@allure.title("Создание задачи")
def test_create_task(admin_token):
    board_id = create_board(admin_token)
    with allure.step("Подготовить данные задачи"):
        task_data = {
            "title": "Test task",
            "description": "Task for API test",
            "status": "todo",
            "priority": "medium",
            "assignee_id": 0,
        }
    with allure.step("Создать задачу"):
        response = TasksService().create_task(
            board_id=board_id,
            task_data=task_data,
            token=admin_token,
        )
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 201
    with allure.step("Проверить модель задачи"):
        TaskModel(**response.json())


@allure.feature("Tasks API")
@allure.title("Удаление задачи")
def test_delete_task(admin_token):
    board_id = create_board(admin_token)
    with allure.step("Подготовить данные задачи"):
        task_data = {
            "title": "Test task to delete",
            "description": "Task for API test",
            "status": "todo",
            "priority": "medium",
            "assignee_id": 0,
        }
    with allure.step("Создать задачу для удаления"):
        create_response = TasksService().create_task(
            board_id=board_id,
            task_data=task_data,
            token=admin_token,
        )

    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    with allure.step("Удалить задачу"):
        delete_response = TasksService().delete_task(
            board_id=board_id,
            task_id=task_id,
            token=admin_token,
        )
    with allure.step("Проверить статус ответа"):
        assert delete_response.status_code == 204


@allure.feature("Tasks API")
@allure.title("Поиск задач с параметрами")
@pytest.mark.parametrize(
    "q, skip, limit",
    [
        ("Test", 0, 1),
        ("task", 0, 10),
        ("a", 0, 5),
        ("not found_task", 0, 10)
    ],
)
def test_search_tasks_with_params(admin_token, q, skip, limit):
    with allure.step(f"Выполнить поиск задач по запросу: {q}"):
        response = TasksService().search_tasks(
            token=admin_token, q=q, skip=skip, limit=limit)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить структуру данных"):
        tasks = response.json()
    if tasks:
        TaskModel(**tasks[0])


@allure.feature("Tasks API")
@allure.title("Создание задачи без названия")
def test_create_task_without_title(admin_token):
    board_id = create_board(admin_token)

    with allure.step("Подготовить данные задачи без названия"):
        task_data = {
            "title": "",
            "description": "Task for API test",
            "status": "todo",
            "priority": "medium",
            "assignee_id": 0,
        }
    with allure.step("Отправить запрос на создание задачи"):
        response = TasksService().create_task(
            board_id=board_id,
            task_data=task_data,
            token=admin_token,
        )
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Tasks API")
@allure.title("Создание задачи с некорректным статусом")
def test_create_task_with_invalid_status(admin_token):
    board_id = create_board(admin_token)
    with allure.step("Подготовить данные с некорректным статусом"):
        task_data = {
            "title": "Test task",
            "description": "Task for API test",
            "status": "invalid_status",
            "priority": "medium",
            "assignee_id": 0,
        }

    with allure.step("Отправить запрос на создание задачи"):
        response = TasksService().create_task(
            board_id=board_id,
            task_data=task_data,
            token=admin_token,
        )
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Tasks API")
@allure.title("Создание задачи с некорректным приоритетом")
def test_create_task_with_invalid_priority(admin_token):
    board_id = create_board(admin_token)
    with allure.step("Подготовить данные с некорректным приоритетом"):
        task_data = {
            "title": "Test task",
            "description": "Task for API test",
            "status": "todo",
            "priority": "invalid_priority",
            "assignee_id": 0,
        }
    with allure.step("Отправить запрос на создание задачи"):
        response = TasksService().create_task(
            board_id=board_id,
            task_data=task_data,
            token=admin_token,
        )
    with allure.step("Проверить ошибку валидации"):
        assert response.status_code == 422


@allure.feature("Tasks API")
@allure.title("Удаление задачи с несуществующим id")
def test_delete_task_with_invalid_id(admin_token):
    board_id = create_board(admin_token)
    with allure.step("Отправить запрос на удаление несуществующей задачи"):
        response = TasksService().delete_task(
            board_id=board_id,
            task_id=999,
            token=admin_token,
        )
    with allure.step("Проверить, что задача не найдена"):
        assert response.status_code == 404


@allure.feature("Tasks API")
@allure.title("Поиск несуществующей задачи")
def test_search_tasks_not_found(admin_token):
    with allure.step("Выполнить поиск несуществующей задачи"):
        response = TasksService().search_tasks(
            token=admin_token,
            q="test123",
            skip=0,
            limit=10,
        )
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
    with allure.step("Проверить пустой результат поиска"):
        assert response.json() == []
