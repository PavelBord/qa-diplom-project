from services.http_client import HttpClient
from config import API_URL


class UsersService():
    def __init__(self) -> None:
        self.client = HttpClient(API_URL)

    def get_users(
        self,
        token: str,
        skip: int = 0,
        limit: int = 100,
    ):
        return self.client.get(
            "/users/",
            params={
                "skip": skip,
                "limit": limit
            },
            headers=self.client.get_headers(token),
        )

    def update_user(
        self,
        user_id: int,
        user_data: dict,
        token: str,
    ):
        return self.client.put(
            f"/users/{user_id}",
            json=user_data,
            headers=self.client.get_headers(token),
        )

    def delete_user(
        self,
        user_id: int,
        token: str,
    ):
        return self.client.delete(
            f"/users/{user_id}",
            headers=self.client.get_headers(token),
        )
