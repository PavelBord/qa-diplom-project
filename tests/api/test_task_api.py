import pytest
from services.boards_service import BoardsService
from services.tasks_service import TasksService
from models.task_model import TaskModel


def test_get_tasks(admin_token):
    board_id = create_board(admin_token)

    response = TasksService().get_tasks(board_id=board_id, token=admin_token)

    assert response.status_code == 200

    tasks = response.json()

    if tasks:
        TaskModel(**tasks[0])


def create_board(admin_token):
    board_data = {
        "title": "Board for task tests",
        "description": "Board created from API test",
        "public": True,
    }

    response = BoardsService().create_board(admin_token, board_data)

    assert response.status_code == 201

    return response.json()["id"]


def test_create_task(admin_token):
    board_id = create_board(admin_token)

    task_data = {
        "title": "Test task",
        "description": "Task for API test",
        "status": "todo",
        "priority": "medium",
        "assignee_id": 0,
    }

    response = TasksService().create_task(
        board_id=board_id,
        task_data=task_data,
        token=admin_token,
    )

    assert response.status_code == 201

    TaskModel(**response.json())


def test_delete_task(admin_token):
    board_id = create_board(admin_token)

    task_data = {
        "title": "Test task to delete",
        "description": "Task for API test",
        "status": "todo",
        "priority": "medium",
        "assignee_id": 0,
    }

    create_response = TasksService().create_task(
        board_id=board_id,
        task_data=task_data,
        token=admin_token,
    )

    assert create_response.status_code == 201
    task_id = create_response.json()["id"]
    delete_response = TasksService().delete_task(
        board_id=board_id,
        task_id=task_id,
        token=admin_token,
    )

    assert delete_response.status_code == 204


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
    response = TasksService().search_tasks(
        token=admin_token, q=q, skip=skip, limit=limit)
    assert response.status_code == 200
    tasks = response.json()
    if tasks:
        TaskModel(**tasks[0])


def test_create_task_without_title(admin_token):
    board_id = create_board(admin_token)

    task_data = {
        "title": "",
        "description": "Task for API test",
        "status": "todo",
        "priority": "medium",
        "assignee_id": 0,
    }

    response = TasksService().create_task(
        board_id=board_id,
        task_data=task_data,
        token=admin_token,
    )

    assert response.status_code == 422


def test_create_task_with_invalid_status(admin_token):
    board_id = create_board(admin_token)

    task_data = {
        "title": "Test task",
        "description": "Task for API test",
        "status": "invalid_status",
        "priority": "medium",
        "assignee_id": 0,
    }

    response = TasksService().create_task(
        board_id=board_id,
        task_data=task_data,
        token=admin_token,
    )

    assert response.status_code == 422


def test_create_task_with_invalid_priority(admin_token):
    board_id = create_board(admin_token)

    task_data = {
        "title": "Test task",
        "description": "Task for API test",
        "status": "todo",
        "priority": "invalid_priority",
        "assignee_id": 0,
    }

    response = TasksService().create_task(
        board_id=board_id,
        task_data=task_data,
        token=admin_token,
    )

    assert response.status_code == 422


def test_delete_task_with_invalid_id(admin_token):
    board_id = create_board(admin_token)

    response = TasksService().delete_task(
        board_id=board_id,
        task_id=999,
        token=admin_token,
    )

    assert response.status_code == 404


def test_search_tasks_not_found(admin_token):
    response = TasksService().search_tasks(
        token=admin_token,
        q="test123",
        skip=0,
        limit=10,
    )

    assert response.status_code == 200
    assert response.json() == []
