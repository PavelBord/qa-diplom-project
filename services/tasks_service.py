from services.http_client import HttpClient
from config import API_URL


class TasksService():
    def __init__(self) -> None:

        self.client = HttpClient(API_URL)

    def get_tasks(
        self,
            board_id: int,
            token: str,
            status: str | None = None,
            priority: str | None = None,
    ):
        return self.client.get(
            f"/boards/{board_id}/tasks",
            params={
                "status": status,
                "priority": priority,
            },
            headers=self.client.get_headers(token),
        )

    def create_task(
        self,
        board_id: int,
        task_data: dict,
        token: str,
    ):
        return self.client.post(
            f"/boards/{board_id}/tasks",
            json=task_data,
            headers=self.client.get_headers(token),
        )

    def search_tasks(
        self,
        token: str,
        q: str,
        skip: int,
        limit: int = 100,
    ):
        return self.client.get(
            "/tasks/search",
            params={
                "q": q,
                "skip": skip,
                "limit": limit,
            },
            headers=self.client.get_headers(token),
        )

    def delete_task(
        self,
        board_id: int,
        task_id: int,
        token: str,
    ):
        return self.client.delete(
            f"/boards/{board_id}/tasks/{task_id}",
            headers=self.client.get_headers(token),
        )
