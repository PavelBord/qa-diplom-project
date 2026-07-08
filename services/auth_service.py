from services.http_client import HttpClient
from config import API_URL


class AuthService:
    def __init__(self) -> None:
        self.client = HttpClient(API_URL)

    def login(self, email: str, password: str):
        return self.client.post("/auth/login", json={"email": email, "password": password})
