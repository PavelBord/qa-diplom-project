from services.http_client import HttpClient
from config import API_URL


class BoardsService:
    def __init__(self) -> None:
        self.client = HttpClient(API_URL)

    def get_headers(self, token: str) -> dict:
        return {"Authorization": f"Bearer {token}"}

    def get_boards(self, token: str):
        return self.client.get("/boards", headers=self.get_headers(token))

    def create_board(self, token: str, board_data: dict):
        return self.client.post("/boards/", json=board_data, headers=self.get_headers(token))
